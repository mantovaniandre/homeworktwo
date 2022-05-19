from Database.connection import MySQLDatabase
from Database.creating_data_base import CreatingDataBase
from Database.inserting_data_into_the_database import InsertingDataIntoTheDatabase
from Environment.environment import DATA_BASE
from Response.bad_request import bad_request
from Response.internal_server_error import internal_server_error
from Response.success import success
from Lambda.lambda_manager import LambdaManager


def lambda_handler():
    try:
    
        db = MySQLDatabase()
        print("DB: ", db)
        
        lambda_manager = LambdaManager(
            CreatingDataBase(),
            InsertingDataIntoTheDatabase()
        )
        
        response = lambda_manager.handle(db)
        
        
        if response is None:
            return bad_request()
        else:
            return success({"msg": "success"})
        
    except Exception as e:
        print("[INFO] ERROR: ", e)
        return internal_server_error()