from app.core.extensions import db
from sqlalchemy import Column, DateTime, Integer, Float


class TimerModel(db.Model):
    __tablename__ = 'timer'

    id = Column(Integer, primary_key=True, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    general_hours = Column(Float, nullable=False)

    task_id = Column(Integer, db.ForeignKey('task.id'), nullable=False)
    task = db.relationship('TaskModel', back_populates='timers')