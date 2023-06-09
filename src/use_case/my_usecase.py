from typing import Type
from src.interfaces import database

class MyUsecase:
    
    def __init__(self, database: Type[database]):
        self.database = database
    
    def search_something(self):
        # Processing
        self.database.select()
    
    def insert_something(self):
        # Processing
        self.database.insert()
