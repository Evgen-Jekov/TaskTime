from abc import ABC, abstractmethod
from app.serialization.serialization import SerializerBase, DeserializerBase
from app.repository.database_abc import AddDB


class ServiceAddBase(ABC):
    @abstractmethod
    def add(self, ser : SerializerBase, der : DeserializerBase, fn_add : AddDB, data, sh):
        pass