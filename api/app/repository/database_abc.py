from abc import abstractmethod, ABC

class AddDB(ABC):
    @abstractmethod
    def add_db(self, object):
        pass

class UpdateDB(ABC):
    @abstractmethod
    def update_db(self, id, obj):
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
    def search_db_by_category_all(self, category_id):
        pass


class SearchTimerDB(ABC):
    @abstractmethod
    def search_db_by_id(self, id):
        pass

    @abstractmethod
    def search_db_by_task(self, task_id):
        pass

class HashingDB(ABC):
    @abstractmethod
    def hash_password(self, password):
        pass

    @abstractmethod
    def hash_password_check(self, password, hspassword):
        pass

class CheckDB(ABC):
    @abstractmethod
    def check_by_username(self, username, email):
        pass

class AddDBUser(ABC):
    @abstractmethod
    def add_db(self, hash, check, obj):
        pass