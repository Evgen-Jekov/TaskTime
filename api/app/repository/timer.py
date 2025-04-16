from sqlalchemy.exc import SQLAlchemyError
from app.core.extensions import db
from app.repository.database_abc import DeleteDB, SearchTimerDB, UpdateDB
from app.model.timer_model import TimerModel
from app.repository.auxiliary import check_data_id, update_data, check_data_task_id

class DeleteTimer(DeleteDB):
    def delete_db(self, id):
        try:
            timer = check_data_id(model=TimerModel, id=id)

            db.session.delete(timer)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise SQLAlchemyError(str(e))

class UpdateTimer(UpdateDB):
    def update_db(self, id, obj : dict):
        try:
            timer = check_data_id(model=TimerModel, id=id)

            res = update_data(model=timer, obj=obj)

            db.session.commit()

            return res
        except SQLAlchemyError as e:
            db.session.rollback()
            raise SQLAlchemyError(str(e))
        

class SearchTimer(SearchTimerDB):
    def search_db_by_id(self, id):
        try:
            timer = check_data_id(model=TimerModel, id=id)
            
            return timer
        except SQLAlchemyError as e:
            raise SQLAlchemyError(str(e))
        
    def search_db_by_task(self, task_id):
        try:
            timer = check_data_task_id(model=TimerModel, task_id=task_id)
            
            return timer
        except SQLAlchemyError as e:
            raise SQLAlchemyError(str(e))
