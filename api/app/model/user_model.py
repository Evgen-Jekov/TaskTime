from app.core.extensions import db
from sqlalchemy import Column, String, Integer

class UserModel(db.Model):
    __tablename__ = 'user_task'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(length=256), nullable=False, unique=True)
    email = Column(String(length=256), nullable=False, unique=True)
    password = Column(String(length=128), nullable=False)

    tasks = db.relationship('TaskModel', back_populates='user', cascade='all, delete-orphan') 

