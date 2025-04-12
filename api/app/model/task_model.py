from app.core.extensions import db
from sqlalchemy import Column, String, Integer, Date, Text

class TaskModel(db.Model):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, nullable=False)
    name_task = Column(String(256), nullable=False)
    task_description = Column(Text(1024), nullable=False)
    state_task = Column(String(32), nullable=False)
    deadline = Column(Date, nullable=True)

    category_id = Column(Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', back_populates='tasks')

    timers = db.relationship('TimerModel', back_populates='task', cascade='all, delete-orphan')