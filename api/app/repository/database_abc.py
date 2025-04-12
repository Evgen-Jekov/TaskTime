from abc import abstractmethod

class AddDB:
    @abstractmethod
    def add_db(self, object):
        pass

class UpdateDB:
    @abstractmethod
    def update_db(self, object):
        pass

class DeleteDB:
    @abstractmethod
    def delete_db(self, id):
        pass

class SearchDB:
    @abstractmethod
    def search_db_by_id(self, id):
        pass

    def search_db_by_name(self, name):
        pass