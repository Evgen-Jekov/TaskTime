from flask_restful import Resource
from app.service.service import ServiceUserRegister
from app.repository.user import AddUser, HashingPassword, CheckUser
from app.serialization.serialization import SerializerAll, DeserializerAll
from app.schemes.user_schemas import UserSchemes
from app.service.service import ServiceJWT
from flask import request

class UserLoginRoute(Resource):
    pass

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
    pass