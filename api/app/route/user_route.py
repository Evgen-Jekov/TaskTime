from flask_restful import Resource
from app.service.service import ServiceAdd, ServiceDelete, ServiceSearchDBAll, ServiceUpdate
from app.repository.user import DeleteUser, SearchUser
from app.repository.add import AddEssence


class UserLoginRoute(Resource):
    pass

class UserRegisterRoute(Resource):
    pass


class UserLogoutRoute(Resource):
    pass

class UserDataUpdateRoute(Resource):
    pass

class UserDeleteRoute(Resource):
    pass