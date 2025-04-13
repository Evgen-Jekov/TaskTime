from abc import ABC, abstractmethod

class DeserializerBase(ABC):
    @abstractmethod
    def load_json(self, data: dict):
        pass

class SerializerBase(ABC):
    @abstractmethod
    def to_json(self, obj):
        pass