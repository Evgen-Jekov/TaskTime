from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime
from abc import abstractmethod

db = SQLAlchemy()

class BaseDB:
    @abstractmethod
    def add_database(self, new_data):
        pass

    @abstractmethod
    def delete_database(self, id_data):
        pass

    @abstractmethod
    def update_data(self, model_update):
        pass
    
    @abstractmethod
    def search_database(self, id_data):
        pass

class TaskDataBase(BaseDB):
    def __init__(self):
        self.db = db