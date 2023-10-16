import os

import pyodbc


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
new_database_name = 'TestProject'

# Define the connection string for the 'master' database
master_connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE=master;UID={username};PWD={password}'

# Connect to the 'master' database
master_connection = pyodbc.connect(master_connection_string, autocommit=True)
master_cursor = master_connection.cursor()

# Create a new database called "TestProject" if it doesn't exist
master_cursor.execute(f"IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = '{new_database_name}') CREATE DATABASE {new_database_name}")
# master_connection.commit()

# Close the 'master' database connection
master_connection.close()
