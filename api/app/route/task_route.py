from flask_restful import Resource
from app.service.service import ServiceAdd
from app.serialization.serialization import SerializerAll, DeserializerAll
from app.repository.add import AddDB
from app.schemes.task_schemes import TaskSchemes

class TaskAddRoute(Resource):
    def post(self, data):
        ser = SerializerAll()
        der = DeserializerAll()
        fn_add = AddDB()

        return {'detail' : ServiceAdd().add(ser=ser, der=der, fn_add=fn_add, data=data, sh=TaskSchemes),
                'state' : 'Succsses'}