from app.route.task_route import TaskAddRoute, TaskDeleteRoute, TaskSearchIDRoute, TaskSearchNameRoute, TaskUpdateRoute
from app.route.category_route import CategoryAddRoute, CategoryDeleteRoute, CategoryUpdateRoute, CategorySearchAllRoute, CategorySearchIDRoute
from app.route.timer_route import TimerAddRoute, TimerDeleteRoute, TimerSearchIDRoute, TimerSearchTaskIDRoute, TimerUpdateRoute
from flask_restful import Api

def connect_route(api : Api):
    api.add_resource(TaskAddRoute, '/task-add')
    api.add_resource(CategoryAddRoute, '/category-add')
    api.add_resource(TimerAddRoute, '/timer-add')

    api.add_resource(TaskDeleteRoute, '/task-delete/<int:id>')
    api.add_resource(CategoryDeleteRoute, '/category-delete/<int:id>')
    api.add_resource(TimerDeleteRoute, '/timer-delete/<int:id>')

    api.add_resource(TaskUpdateRoute, '/task-update/<int:id>')
    api.add_resource(CategoryUpdateRoute, '/category-update/<int:id>')
    api.add_resource(TimerUpdateRoute, '/timer-update/<int:id>')

    api.add_resource(TaskSearchNameRoute, '/task-search-by-name/<string:name>')
    api.add_resource(TaskSearchIDRoute, '/task-search-by-id/<int:id>')
    api.add_resource(CategorySearchIDRoute, '/category-search-by-id/<int:id>')
    api.add_resource(CategorySearchAllRoute, '/category-search-all/<int:category_id>')
    api.add_resource(TimerSearchIDRoute, '/timer-search-by-id/<int:id>')
    api.add_resource(TimerSearchTaskIDRoute, '/timer-search-by-task-id/<int:task_id>')