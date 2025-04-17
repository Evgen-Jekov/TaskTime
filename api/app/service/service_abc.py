from abc import ABC, abstractmethod
from app.serialization.serialization import SerializerBase, DeserializerBase
from app.repository.database_abc import AddDB, DeleteDB, UpdateDB, SearchDB


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