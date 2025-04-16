from flask_restful import Resource
from flask import request
from app.service.service import ServiceAdd, ServiceDelete
from app.serialization.serialization import SerializerAll, DeserializerAll
from app.repository.add import AddEssence
from app.repository.timer import DeleteTimer
from app.schemes.timer_schemes import TimerSchemes


class TimerAddRoute(Resource):
    def post(self):
        data = request.get_json()
        ser = SerializerAll()
        der = DeserializerAll()
        fn_add = AddEssence()

        return {'detail' : ServiceAdd().add(ser=ser, der=der, fn_add=fn_add, data=data, sh=TimerSchemes)}, 201
    
class TimerDeleteRoute(Resource):
    def delete(self, id):
        fn_del = DeleteTimer()

        return {'detail' : ServiceDelete().delete(fn_del=fn_del, id=id)}, 200