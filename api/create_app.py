from flask import Flask
from flask_restful import Api
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    api = Api(app=app)
    CORS(app=app)

    return app