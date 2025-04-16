from app.route.task_route import TaskAddRoute, TaskDeleteRoute
from app.route.category_route import CategoryAddRoute, CategoryDeleteRoute
from app.route.timer_route import TimerAddRoute, TimerDeleteRoute
from flask_restful import Api

def connect_route(api : Api):
    api.add_resource(TaskAddRoute, '/task-add')
    api.add_resource(CategoryAddRoute, '/category-add')
    api.add_resource(TimerAddRoute, '/timer-add')

    api.add_resource(TaskDeleteRoute, '/task-delete/<int:id>')
    api.add_resource(CategoryDeleteRoute, '/category-delete/<int:id>')
    api.add_resource(TimerDeleteRoute, '/timer-delete/<int:id>')