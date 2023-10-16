import os
import pyodbc
from datetime import datetime
import hashlib


def is_running_in_docker():
    # Check for common Docker environment variables
    return (
        os.environ.get("DOCKER_CONTAINER") == "true" or
        os.environ.get("DOCKER") == "true" or
        os.path.exists("/.dockerenv") or
        os.path.exists("/.dockerinit")
    )


# Define your server and authentication details
if is_running_in_docker():
    server = "sqlazure"
else:
    server = "localhost"

username = 'SA'
password = 'password@1234'
database_name = 'TestProject'

# Define the connection string for the "TestProject" database
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database_name};UID={username};PWD={password}'


# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Go two directories back
root_directory = os.path.abspath(os.path.join(script_directory, "..", ".."))
sql_scripts_directory = os.path.join(root_directory, "src/takeons")

# List all SQL script files in the directory
sql_files = [f for f in os.listdir(sql_scripts_directory) if f.endswith('.sql')]

# Sort SQL script files by their date in ascending order
sql_files.sort()

# Connect to the "TestProject" database
connection = pyodbc.connect(connection_string, autocommit=True)
cursor = connection.cursor()

# Create the Flyway schema history table if it doesn't exist in "TestProject"
cursor.execute('''
    IF NOT EXISTS (SELECT 1 FROM sysobjects WHERE name = 'FlywaySchemaHistory' AND xtype = 'U')
    BEGIN
        CREATE TABLE FlywaySchemaHistory (
            id INT IDENTITY(1,1) NOT NULL,
            version VARCHAR(50) NOT NULL,
            description VARCHAR(200) NULL,
            type VARCHAR(20) NOT NULL,
            script VARCHAR(1000) NOT NULL,
            checksum NVARCHAR(100),
            installed_by VARCHAR(100) NOT NULL,
            installed_on DATETIME NOT NULL,
            execution_time INT NOT NULL,
            success BIT NOT NULL
        );
    END
''')
# connection.commit()

# Loop through and execute SQL scripts
for sql_file in sql_files:
    sql_file_path = os.path.join(sql_scripts_directory, sql_file)

    with open(sql_file_path, 'r') as file:
        sql_script = file.read()

    # Calculate the checksum of the SQL script
    checksum = hashlib.md5(sql_script.encode()).hexdigest()

    # Check if the script is already in the Flyway schema history
    cursor.execute("SELECT COUNT(*) FROM FlywaySchemaHistory WHERE script = ?", sql_file)
    if cursor.fetchone()[0] == 0:
        # If not, insert it into the Flyway history
        cursor.execute(
            "INSERT INTO FlywaySchemaHistory (version, type, script, checksum, installed_by, installed_on, execution_time, success) VALUES (?, ?, ?, ?, ?, ?, 0, 1)",
            (sql_file, 'SQL', sql_file, checksum, 'PythonScript', datetime.now()))
        # connection.commit()

        # Execute the SQL script
        cursor.execute(sql_script)
        # connection.commit()

        print(f"Executed script: {sql_file}")
    else:
        print(f"Skipping script: {sql_file} (Already executed)")

# Close the "TestProject" database connection
connection.close()
