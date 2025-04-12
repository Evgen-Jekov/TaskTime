from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.connect.connector import ConnectExtension
from config import Config

def create_app():
    app = Flask(__name__)
    api = Api(app=app)
    CORS(app=app)
    app.config.from_object(Config)

    connect_ex = ConnectExtension()
    connect_ex.connect(app=app)

    return app