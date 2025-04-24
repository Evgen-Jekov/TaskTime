from app.service.service_abc import ServiceAddBase, ServiceDeleteBase, ServiceUpdateBase, ServiceSearchBase, ServiceSearchCategoryBase, ServiceSearchTimerBase, ServiceRegisterUserBase, ServiceJWTBase, ServiceLoginUserBase
from app.serialization.serialization import SerializerBase, DeserializerBase
from app.repository.database_abc import AddDB, DeleteDB, UpdateDB, SearchDB, SearchCategory, SearchTimerDB, HashingDB, CheckDB, AddDBUser
from flask_jwt_extended import create_access_token
from datetime import timedelta

class ServiceAdd(ServiceAddBase):
    def add(self, ser : SerializerBase, der : DeserializerBase, fn_add : AddDB, data, sh):
        odj = der.load_json(data=data, sh=sh)

        fn_add.add_db(odj)

        return ser.to_json(odj, sh=sh)
    
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
    

class ServiceSearchCategory(ServiceSearchCategoryBase):
    def search_category_all(self, ser : SerializerBase, category_id, fn_search : SearchCategory, sh):
        res = fn_search.search_db_by_category_all(category_id=category_id)

        return ser.to_json(obj=res, sh=sh)
    
    def search_category_id(self, ser : SerializerBase, id, fn_search : SearchCategory, sh):
        res = fn_search.search_db_by_id(id=id)

        return ser.to_json(obj=res, sh=sh)
    
class ServiceSearchTimer(ServiceSearchTimerBase):
    def search_id(self, ser : SerializerBase, id, fn_search : SearchTimerDB, sh):
        res = fn_search.search_db_by_id(id=id)

        return ser.to_json(obj=res, sh=sh)
    
    def search_task_id(self, ser : SerializerBase, task_id, fn_search : SearchTimerDB, sh):
        res = fn_search.search_db_by_task(task_id=task_id)

        return ser.to_json(obj=res, sh=sh)
    
class ServiceUserRegister(ServiceRegisterUserBase):
    def register_user(self, ser : SerializerBase, der : DeserializerBase, fn_add : AddDBUser,
                   fn_hash : HashingDB, fn_check : CheckDB, 
                   data, sh):
        obj = der.load_json(data=data, sh=sh)

        res = fn_add.add_db(hash=fn_hash, check=fn_check, obj=obj)

        return {'detail' : ser.to_json(obj=res, sh=sh), 'token' : ServiceJWT().create_jwt(user_id=res.id)}
    
class ServiceUserLogin(ServiceLoginUserBase):
    def login_user(self, ser : SerializerBase, der : DeserializerBase, fn_sh : SearchDB, data, sh):
        obj = der.load_json(data=data, sh=sh)

        res = fn_sh.search_db_by_name(name=obj.username)

        return {'detail' : ser.to_json(obj=res, sh=sh), 'token' : ServiceJWT().create_jwt(user_id=res.id)}

class ServiceJWT(ServiceJWTBase):
    def create_jwt(self, user_id):
        return create_access_token(identity=user_id, expires_delta=timedelta(days=1))