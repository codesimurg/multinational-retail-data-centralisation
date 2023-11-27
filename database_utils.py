
import yaml
from sqlalchemy import create_engine, text
from sqlalchemy import inspect

class DatabaseConnector:
	
    
    def __init__(self):
	self.creds = {}
    
    def read_db_creds(self):
        with open('db_creds.yaml') as yaml_file:
            self_creds = yaml.safe_load(file)
        return self_creds
    
    def init_db_engine(self):
        self_creds = self.read_db_creds()
        engine = create_engine(f"{'postgresql'}+{'psycopg2'}://{self_creds['RDS_USER']}:{self_creds['RDS_PASSWORD']}@{self_creds['RDS_HOST']}:{self_creds['RDS_PORT']}/{self_creds['RDS_DATABASE']}"
        engine.connect()
        return engine
    
    def list_db_tables(self):
        engine = self.init_db_engine()
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        return table_names
    
    

    