from app.core.extensions import db
from app.model.category_model import CategoryModel
from app.repository.database_abc import DeleteDB, UpdateDB, SearchCategory
from app.model.task_model import TaskModel
from sqlalchemy.exc import SQLAlchemyError

class DeleteCategory(DeleteDB):
    def delete_db(self, id):
        try:
            category = CategoryModel.query.filter(CategoryModel.id  == id).first()

            if category is None:
                raise ValueError('Not found')

            db.session.delete(category)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError
        
class UpdateCategory(UpdateDB):
    def update_db(self, id, object : dict):
        try:
            category = CategoryModel.query.filter(CategoryModel.id == id).first()

            if category is None:
                raise ValueError('Not found')
            
            for key, value, in object.items():
                if hasattr(category, key):
                    setattr(category, key, value)
            
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError

class SearchTaskCategory(SearchCategory):
    def search_db_by_category_all(self, category_id):
        try:
            all_task = TaskModel.query.filter(TaskModel.category_id == category_id).all()

            if not all_task:
                raise ValueError('Not found')

            return all_task
        except SQLAlchemyError:
            raise SQLAlchemyError
        
    def search_db_by_id(self, id):
        try:
            category = CategoryModel.query.filter(CategoryModel.id == id).first()

            if category is None:
                raise ValueError('Not found')
            
            return category
        except SQLAlchemyError:
            raise SQLAlchemyError