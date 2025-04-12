from abc import abstractmethod

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