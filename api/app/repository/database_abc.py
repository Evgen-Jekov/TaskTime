from abc import abstractmethod, ABC

class AddDB(ABC):
    @abstractmethod
    def add_db(self, object):
        pass

class UpdateDB(ABC):
    @abstractmethod
    def update_db(self, id, object):
        pass

class DeleteDB(ABC):
    @abstractmethod
    def delete_db(self, id):
        pass

class SearchDB(ABC):
    @abstractmethod
    def search_db_by_id(self, id):
        pass

    @abstractmethod
    def search_db_by_name(self, name):
        pass

class SearchCategory(ABC):
    @abstractmethod
    def search_db_by_id(self, id):
        pass

    @abstractmethod
    def search_db_by_category_all(self):
        pass


class SearchTimerDB(ABC):
    @abstractmethod
    def search_db_by_id(self, id):
        pass

    @abstractmethod
    def search_db_by_task(self, task_id):
        pass