from app.model.database import db
from abc import abstractmethod
from flask import Flask
from flask_migrate import Migrate

class Connect:
    @abstractmethod
    def connect(self, app):
        pass

class ConnectExtension(Connect):
    def connect(self, app : Flask):
        db.init_app(app=app)
        migrate = Migrate(app=app, db=db)