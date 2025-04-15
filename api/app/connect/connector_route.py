from app.route.task_route import TaskAddRoute
from flask_restful import Api

def connect_route(api : Api):
    api.add_resource(TaskAddRoute, '/task-add')