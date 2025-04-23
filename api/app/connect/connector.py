from app.route.task_route import TaskAddRoute, TaskDeleteRoute, TaskSearchIDRoute, TaskSearchNameRoute, TaskUpdateRoute
from app.route.category_route import CategoryAddRoute, CategoryDeleteRoute, CategoryUpdateRoute, CategorySearchAllRoute, CategorySearchIDRoute
from app.route.timer_route import TimerAddRoute, TimerDeleteRoute, TimerSearchIDRoute, TimerSearchTaskIDRoute, TimerUpdateRoute
from app.core.extensions import db, ma, jwt
from abc import abstractmethod, ABC
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

class Connect(ABC):
    @abstractmethod
    def connect_ex(self, app):
        pass

    @abstractmethod
    def connect_route(self, api : Api):
        pass

class Connector(Connect):
    def connect_ex(self, app : Flask):
        db.init_app(app=app)
        migrate = Migrate(app=app, db=db)
        ma.init_app(app=app)
        jwt.init_app(app=app)

    def connect_route(self, api : Api):
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