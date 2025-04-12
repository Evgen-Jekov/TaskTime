from app.core.extensions import db
from app.repository.database_abc import AddDB, DeleteDB, UpdateDB, SearchDB
from sqlalchemy.exc import SQLAlchemyError
from app.model.task_model import TaskModel

class AddTask(AddDB):
    def add_db(self, object : TaskModel):
        try:
            db.session.add(object)
            db.session.commit()

            return True
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError
        
