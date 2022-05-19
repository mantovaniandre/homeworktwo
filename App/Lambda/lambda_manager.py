from Database.creating_data_base import CreatingDataBase
from Database.inserting_data_into_the_database import InsertingDataIntoTheDatabase

class LambdaManager:
    
    def __init__(
        self,
        creating_database,
        inserting_data_into_the_Database
        
    ):
        self.creating_database = creating_database,
        self.inserting_data_into_the_Database = inserting_data_into_the_Database,

        
    def handle(self, db):
        creatingDataBase = CreatingDataBase.creatingDataBase(db)
        inserting_data_into_the_Database = InsertingDataIntoTheDatabase.inserting(db)
        return True    