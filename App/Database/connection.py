from typing import Any, List
import dotenv
import traceback
import mysql.connector
from Interface.interface_database import DatabaseInterface

dotenv.load_dotenv()

class MySQLDatabase(DatabaseInterface):
    
    # def instance(cls):
    #     pass
    
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='esocial',
            port=4556
        )
        print("Self COnnection: ", self.connection)
        self.cursor = self.connection.cursor(dictionary=True)
        print("Self Cursor: ", self.cursor)
    
    def execute_query(self, query: str, params: List[Any] = []):
        try:
            self.cursor.execute(query, params)
            
        except Exception as e:
            print(f'[INFO] ERROR: ', e)
            traceback.print_exc()
            raise e
        
        result = self.cursor.fetchall()
        
        if result is not None:
            return result
        else:
            return[]
    
    def close(self):
        self.cursor.close()
        self.connection.close()
        self.connection = None
    
    def commit(self):
        self.connection.commit()
    
    def rollback(self):
        self.connection.rollback()
        