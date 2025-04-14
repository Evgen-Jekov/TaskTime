from app.core.extensions import db
from app.model.category_model import CategoryModel
from app.repository.database_abc import DeleteDB, UpdateDB, SearchCategory
from app.model.task_model import TaskModel
from sqlalchemy.exc import SQLAlchemyError
from app.repository.auxiliary import check_data_id, update_data, check_data_category_id

class DeleteCategory(DeleteDB):
    def delete_db(self, id):
        try:
            category = check_data_id(model=CategoryModel, id=id)

            db.session.delete(category)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError
        finally:
            db.session.close()
        
class UpdateCategory(UpdateDB):
    def update_db(self, id, obj : dict):
        try:
            category = check_data_id(model=CategoryModel, id=id)
            
            update_data(model=category, obj=obj)
            
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError
        finally:
            db.session.close()

class SearchTaskCategory(SearchCategory):
    def search_db_by_category_all(self, category_id):
        try:
            all_task = check_data_category_id(model=CategoryModel, category_id=category_id)

            return all_task
        except SQLAlchemyError:
            raise SQLAlchemyError
        finally:
            db.session.close()
        
    def search_db_by_id(self, id):
        try:
            category = check_data_id(model=CategoryModel, id=id)
            
            return category
        except SQLAlchemyError:
            raise SQLAlchemyError
        finally:
            db.session.close()