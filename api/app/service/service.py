from app.service.service_abc import ServiceAddBase, ServiceDeleteBase, ServiceUpdateBase, ServiceSearchBase
from app.serialization.serialization import SerializerBase, DeserializerBase
from app.repository.database_abc import AddDB, DeleteDB, UpdateDB, SearchDB
from typing import Union

class ServiceAdd(ServiceAddBase):
    def add(self, ser : SerializerBase, der : DeserializerBase, fn_add : AddDB, data, sh):
        task = der.load_json(data=data, sh=sh)

        fn_add.add_db(task)

        return ser.to_json(task, sh=sh)
    
class ServiceDelete(ServiceDeleteBase):
    def delete(self, fn_del : DeleteDB, id):
        fn_del.delete_db(id=id)

        return {'detail' : 'Succsses'}
    
class ServiceUpdate(ServiceUpdateBase):
    def update(self, ser : SerializerBase, fn_update : UpdateDB, id, data, sh):
        res = fn_update.update_db(id=id, obj=data)

        return ser.to_json(res, sh=sh)
    
class ServiceSearchDBAll(ServiceSearchBase):
    def search_id(self, ser : SerializerBase, id, fn_search : SearchDB, sh):
        res = fn_search.search_db_by_id(id=id)

        return ser.to_json(obj=res, sh=sh)

    def search_name(self, ser : SerializerBase, name, fn_search : SearchDB, sh):
        res = fn_search.search_db_by_name(name=name)

        return ser.to_json(obj=res, sh=sh)