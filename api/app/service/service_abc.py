from abc import ABC, abstractmethod
from app.serialization.serialization import SerializerBase, DeserializerBase
from app.repository.database_abc import AddDB, DeleteDB, UpdateDB, SearchDB, SearchCategory, SearchTimerDB
from app.repository.database_abc import HashingDB, CheckDB

class ServiceAddBase(ABC):
    @abstractmethod
    def add(self, ser : SerializerBase, der : DeserializerBase, fn_add : AddDB, data, sh):
        pass

class ServiceDeleteBase(ABC):
    @abstractmethod
    def delete(self, fn_del : DeleteDB, id):
        pass

class ServiceUpdateBase(ABC):
    @abstractmethod
    def update(self, ser : SerializerBase, der : DeserializerBase, fn_update : UpdateDB, id, data, sh):
        pass

class ServiceSearchBase(ABC):
    @abstractmethod
    def search_id(self, ser : SerializerBase, id, fn_search : SearchDB, sh):
        pass
    
    @abstractmethod
    def search_name(self, ser : SerializerBase, name, fn_search : SearchDB, sh):
        pass

class ServiceSearchCategoryBase(ABC):
    @abstractmethod
    def search_category_all(self, ser : SerializerBase, category_id, fn_search : SearchCategory, sh):
        pass

    def search_category_id(self, ser : SerializerBase, id, fn_search : SearchCategory, sh):
        pass


class ServiceSearchTimerBase(ABC):
    @abstractmethod
    def search_id(self, ser : SerializerBase, id, fn_search : SearchTimerDB, sh):
        pass

    def search_task_id(self, ser : SerializerBase, task_id, fn_search : SearchTimerDB, sh):
        pass


class ServiceRegisterUserBase(ABC):
    @abstractmethod
    def register_user(self, ser : SerializerBase, der : DeserializerBase, 
                   fn_add : AddDB, data, sh, 
                   fn_hash_check : HashingDB, check : CheckDB):
        pass

class ServiceJWTBase(ABC):
    @abstractmethod
    def create_jwt(self, user_id):
        pass