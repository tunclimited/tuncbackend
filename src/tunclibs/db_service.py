from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseService:
    def __init__(self):
        # Configure the database connection
        db_uri = 'mssql+pyodbc://SA:password%401234@localhost:1433/TestProject?driver=ODBC+Driver+17+for+SQL+Server'
        self.engine = create_engine(db_uri, echo=True)  # Set echo to True for SQL query logging
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        # Return a session object
        return self.Session()
