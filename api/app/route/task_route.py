from flask_restful import Resource
from app.service.service import ServiceAdd, ServiceDelete, ServiceSearchDBAll
from app.serialization.serialization import SerializerAll, DeserializerAll
from app.repository.add import AddEssence
from app.repository.task import DeleteTask, SearchTask
from app.schemes.task_schemes import TaskSchemes
from flask import request

class TaskAddRoute(Resource):
    def post(self):
        data = request.get_json()
        ser = SerializerAll()
        der = DeserializerAll()
        fn_add = AddEssence()

        return {'detail' : ServiceAdd().add(ser=ser, der=der, fn_add=fn_add, data=data, sh=TaskSchemes)}, 201
    
class TaskDeleteRoute(Resource):
    def delete(self, id):
        fn_del = DeleteTask()

        return {'detail' : ServiceDelete().delete(fn_del=fn_del, id=id)}, 200
    
class TaskSearchIDRoute(Resource):
    def get(self, id):
        ser = SerializerAll()
        fn_search = SearchTask()

        return {'detail' : ServiceSearchDBAll().search_id(ser=ser, id=id, fn_search=fn_search, sh=TaskSchemes)}, 200
    
class TaskSearchNameRoute(Resource):
    def get(self, name):
        ser = SerializerAll()
        fn_search = SearchTask()

        return {'detail' : ServiceSearchDBAll().search_name(ser=ser, name=name, fn_search=fn_search, sh=TaskSchemes)}, 200