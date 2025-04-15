from api.app.service.service_abc import ServiceAddBase
from app.serialization.serialization import SerializerBase, DeserializerBase
from app.repository.database_abc import AddDB

class ServiceAdd(ServiceAddBase):
    def add(self, ser : SerializerBase, der : DeserializerBase, fn_add : AddDB, data, sh):
        task = der.load_json(data=data, sh=sh)

        fn_add(task)

        return ser.to_json(task)