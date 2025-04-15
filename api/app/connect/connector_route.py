from app.route.task_route import TaskAddRoute
from app.route.category_route import CategoryAddRoute
from flask_restful import Api

def connect_route(api : Api):
    api.add_resource(TaskAddRoute, '/task-add')
    api.add_resource(CategoryAddRoute, '/category-add')