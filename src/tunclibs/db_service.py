from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.tunclibs.docker_networking_helper import is_running_in_docker


class DatabaseService:
    def __init__(self):
        # Configure the database connection
        if is_running_in_docker():
            url = "sqlazure"
        else:
            url = "localhost"

        db_uri = f'mssql+pyodbc://SA:password%401234@{url}:1433/TestProject?driver=ODBC+Driver+17+for+SQL+Server'
        self.engine = create_engine(db_uri, echo=True)  # Set echo to True for SQL query logging
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        # Return a session object
        return self.Session()
