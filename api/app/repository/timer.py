from sqlalchemy.exc import SQLAlchemyError
from app.core.extensions import db
from app.repository.database_abc import DeleteDB, SearchTimerDB, UpdateDB
from app.model.timer_model import TimerModel

class DeleteTimer(DeleteDB):
    def delete_db(self, id):
        try:
            timer = TimerModel.query.filter(TimerModel.id == id).first()

            if timer is None:
                raise ValueError('Not found')

            db.session.delete(timer)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError

class UpdateTimer(UpdateDB):
    def update_db(self, id, object : dict):
        try:
            timer = TimerModel.query.filter(TimerModel.id == id).first()

            if timer is None:
                raise ValueError('Not found')
            
            for key, value, in object.items():
                if hasattr(timer, key):
                    setattr(timer, key, value)

            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError
        

class SearchTimer(SearchTimerDB):
    def search_db_by_id(self, id):
        try:
            timer = TimerModel.query.filter(TimerModel.id == id).first()

            if timer is None:
                raise ValueError('Not Found')
            
            return timer
        except SQLAlchemyError:
            raise SQLAlchemyError
        
    def search_db_by_task(self, task_id):
        try:
            timer = TimerModel.query.filter(TimerModel.task_id == task_id).all()

            if not timer:
                raise ValueError('Not found')
            
            return timer
        except SQLAlchemyError:
            raise SQLAlchemyError
