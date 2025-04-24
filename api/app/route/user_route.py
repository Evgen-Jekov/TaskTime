from flask_restful import Resource
from app.service.service import ServiceUserRegister, ServiceUserLogin, ServiceDelete
from app.repository.user import AddUser, HashingPassword, CheckUser, SearchUser, DeleteUser
from app.serialization.serialization import SerializerAll, DeserializerAll
from app.schemes.user_schemas import UserSchemes
from flask import request

class UserLoginRoute(Resource):
    def post(self):
        data = request.get_json()
        ser = SerializerAll()
        der = DeserializerAll()
        fn_sh = SearchUser()

        return ServiceUserLogin().login_user(ser=ser, der=der, fn_sh=fn_sh, data=data, sh=UserSchemes), 200


class UserRegisterRoute(Resource):
    def post(self):
        data = request.get_json()
        ser = SerializerAll()
        der = DeserializerAll()
        fn_add = AddUser()
        fn_hash = HashingPassword()
        fn_check = CheckUser()

        return ServiceUserRegister().register_user(ser=ser, der=der, 
                                                    fn_add=fn_add, fn_hash=fn_hash,
                                                    fn_check=fn_check, data=data, 
                                                    sh=UserSchemes), 201


class UserLogoutRoute(Resource):
    pass

class UserDataUpdateRoute(Resource):
    pass

class UserDeleteRoute(Resource):
    def delete(self, id):
        fn_del = DeleteUser()

        return ServiceDelete().delete(fn_del=fn_del, id=id)