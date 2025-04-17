from flask_restful import Resource
from app.service.service import ServiceAdd, ServiceDelete, ServiceUpdate, ServiceSearchCategory
from app.serialization.serialization import SerializerAll, DeserializerAll
from app.repository.add import AddEssence
from app.repository.category import DeleteCategory, UpdateCategory, SearchTaskCategory
from app.schemes.category_schemes import CategorySchemes
from flask import request

class CategoryAddRoute(Resource):
    def post(self):
        data = request.get_json()
        ser = SerializerAll()
        der = DeserializerAll()
        fn_add = AddEssence()

        return {'detail' : ServiceAdd().add(ser=ser, der=der, fn_add=fn_add, data=data, sh=CategorySchemes)}, 201
    
class CategoryDeleteRoute(Resource):
    def delete(self, id):
        fn_del = DeleteCategory()

        return {'detail' : ServiceDelete().delete(fn_del=fn_del, id=id)}, 200
    

class CategoryUpdateRoute(Resource):
    def put(self, id):
        data = request.get_json()
        ser = SerializerAll()
        fn_update = UpdateCategory()

        return {'detail' : ServiceUpdate().update(ser=ser, fn_update=fn_update, id=id, data=data, sh=CategorySchemes)}, 200
    
class CategorySearchIDRoute(Resource):
    def get(self, id):
        ser = SerializerAll()
        fn_search = SearchTaskCategory()

        return {'detail' : ServiceSearchCategory().search_category_id(ser=ser, id=id, fn_search=fn_search, sh=CategorySchemes)}, 200
    
class CategorySearchAllRoute(Resource):
        def get(self, category_id):
            ser = SerializerAll()
            fn_search = SearchTaskCategory()

            return {'detail' : ServiceSearchCategory().search_category_all(ser=ser, category_id=category_id, fn_search=fn_search, sh=CategorySchemes)}, 200
