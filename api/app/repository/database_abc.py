from abc import abstractmethod

class AddDB:
    @abstractmethod
    def add_db(self, object):
        pass

class UpdateDB:
    @abstractmethod
    def update_db(self, id, object):
        pass

class DeleteDB:
    @abstractmethod
    def delete_db(self, id):
        pass

class SearchDB:
    @abstractmethod
    def search_db_by_id(self, id):
        pass

    @abstractmethod
    def search_db_by_name(self, name):
        pass

class SearchCategory:
    @abstractmethod
    def search_db_by_id(self, id):
        pass

    @abstractmethod
    def search_db_by_category_all(self):
        pass


class SearchTimerDB:
    @abstractmethod
    def search_db_by_id(self, id):
        pass

    @abstractmethod
    def search_db_by_task(self, task_id):
        pass