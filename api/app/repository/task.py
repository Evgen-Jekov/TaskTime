from app.core.extensions import db
from app.repository.database_abc import DeleteDB, UpdateDB, SearchDB
from sqlalchemy.exc import SQLAlchemyError
from app.model.task_model import TaskModel
from app.repository.auxiliary import check_data_id, update_data, check_data_name
        
class DeleteTask(DeleteDB):
    def delete_db(self, id):
        try:
            task = check_data_id(model=TaskModel, id=id)

            db.session.delete(task)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError
        
class UpdateTask(UpdateDB):
    def update_db(self, id, obj : dict):
        try:
            task = check_data_id(model=TaskModel, id=id)
            
            res = update_data(task, obj=obj)

            db.session.commit()

            return res
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError
        
class SearchTask(SearchDB):
    def search_db_by_id(self, id):
        try:
            task = check_data_id(model=TaskModel, id=id)

            return task
        except SQLAlchemyError:
            raise SQLAlchemyError
        
    def search_db_by_name(self, name):
        try:
            task = check_data_name(model=TaskModel, name=name)

            return task
        except SQLAlchemyError:
            raise SQLAlchemyError