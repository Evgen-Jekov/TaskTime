from abc import ABC, abstractmethod
from marshmallow import ValidationError

class DeserializerBase(ABC):
    @abstractmethod
    def load_json(self, data, sh):
        pass

class SerializerBase(ABC):
    @abstractmethod
    def to_json(self, obj, sh):
        pass

class SerializerBaseMany(ABC):
    @abstractmethod
    def to_json(self, obj, sh):
        pass


class SerializerAll(SerializerBase):
    def to_json(self, obj, sh):
        try:
            return sh().dump(obj)
        except ValidationError:
            raise ValidationError(message='Validate error')
        
class DeserializerAll(DeserializerBase):
    def load_json(self, data, sh):
        try:
            return sh().load(data)
        except ValidationError:
            raise ValidationError(message='Validate error')
        
class SerializerAllMany(SerializerBaseMany):
    def to_json(self, obj, sh):
        try:
            return sh(many=True).dump(obj)
        except ValidationError:
            raise ValidationError(message='Validate error')
        