from flask_restful import Resource
from app.service.service import ServiceAdd
from app.serialization.serialization import SerializerAll, DeserializerAll
from app.repository.add import AddEssence
from app.schemes.category_schemes import CategorySchemes
from flask import request

class CategoryAddRoute(Resource):
    def post(self):
        data = request.get_json()
        ser = SerializerAll()
        der = DeserializerAll()
        fn_add = AddEssence()

        return {'detail' : ServiceAdd().add(ser=ser, der=der, fn_add=fn_add, data=data, sh=CategorySchemes),
                'state' : 'Succsses'}