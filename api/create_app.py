from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.connect.connector import ConnectExtension
from config import Config
from app.model.category_model import CategoryModel
from app.model.task_model import TaskModel
from app.model.timer_model import TimerModel
from app.connect.connector_route import connect_route

def create_app():
    app = Flask(__name__)
    api = Api(app=app)
    CORS(app=app)
    app.config.from_object(Config)

    connect_ex = ConnectExtension()
    connect_ex.connect(app=app)
    connect_route(api=api)

    return app