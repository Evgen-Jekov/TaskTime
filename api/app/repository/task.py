from app.core.extensions import db
from app.repository.database_abc import DeleteDB, UpdateDB, SearchDB
from sqlalchemy.exc import SQLAlchemyError
from app.model.task_model import TaskModel
        
class DeleteTask(DeleteDB):
    def delete_db(self, id):
        try:
            task = TaskModel.query.filter(TaskModel.id == id).first()
            db.session.delete(task)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError
        
class UpdateTask(UpdateDB):
    def update_db(self, id, object : dict):
        try:
            task = TaskModel.query.filter(TaskModel.id == id).filter()

            if task is None:
                raise ValueError('Not found')
            
            for key, value, in object.item():
                if hasattr(task, key):
                    setattr(task, key, value)

            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError
        
class SearchByID(SearchDB):
    def search_db_by_id(self, id):
        try:
            task = TaskModel.query.filter(TaskModel.id == id).first()

            return task
        except SQLAlchemyError:
            raise SQLAlchemyError
        
    def search_db_by_name(self, name):
        try:
            task = TaskModel.query.filter(TaskModel.name_task == name).first()

            return task
        except SQLAlchemyError:
            raise SQLAlchemyError
        
    def search_db_by_category_all(self, category_id):
        try:
            all_task = TaskModel.query.filter(TaskModel.category_id == category_id).all()

            return all_task
        except SQLAlchemyError:
            raise SQLAlchemyError