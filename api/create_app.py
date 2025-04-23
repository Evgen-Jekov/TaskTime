from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import Config
from app.model.category_model import CategoryModel
from app.model.task_model import TaskModel
from app.model.timer_model import TimerModel
from app.model.user_model import UserModel
from app.connect.connector import Connector

def create_app():
    app = Flask(__name__)
    api = Api(app=app)
    CORS(app=app)
    app.config.from_object(Config)

    connect = Connector()
    connect.connect_ex(app=app)
    connect.connect_route(api=api)

    return app