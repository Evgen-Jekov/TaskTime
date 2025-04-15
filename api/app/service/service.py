from app.service.service_abc import ServiceAddBase, ServiceDeleteBase, ServiceUpdateBase
from app.serialization.serialization import SerializerBase, DeserializerBase
from app.repository.database_abc import AddDB, DeleteDB, UpdateDB

class ServiceAdd(ServiceAddBase):
    def add(self, ser : SerializerBase, der : DeserializerBase, fn_add : AddDB, data, sh):
        task = der.load_json(data=data, sh=sh)

        fn_add(task)

        return ser.to_json(task)
    
class ServiceDelete(ServiceDeleteBase):
    def delete(self, fn_del : DeleteDB, id):
        fn_del.delete_db(id=id)

        return {'detail' : 'Succsses'}
    
class ServiceUpdate(ServiceUpdateBase):
    def update(self, ser : SerializerBase, fn_update : UpdateDB, id, data, sh):
        res = fn_update.update_db(id=id, obj=data)

        return ser.to_json(res, sh=sh)