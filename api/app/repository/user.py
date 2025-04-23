from app.repository.database_abc import DeleteDB, UpdateDB, SearchDB
from app.model.user_model import UserModel
from app.repository.auxiliary import check_data_id, check_data_username
from app.core.extensions import db
from sqlalchemy.exc import SQLAlchemyError

class DeleteUser(DeleteDB):
    def delete_db(self, id):
        try:
            user = check_data_id(model=UserModel, id=id)

            db.session.delete(user)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise SQLAlchemyError(str(e))
        

class SearchUser(SearchDB):
    def search_db_by_id(self, id):
        try:
            user = check_data_id(model=UserModel, id=id)

            return user
        except SQLAlchemyError as e:
            raise SQLAlchemyError(str(e))
        
    def search_db_by_name(self, name):
        try:
            user = check_data_username(model=UserModel, name=name)

            return user
        except SQLAlchemyError as e:
            raise SQLAlchemyError(str(e))
