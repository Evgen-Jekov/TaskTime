from app.repository.database_abc import DeleteDB, UpdateDB, SearchDB, HashingDB, CheckDB, AddDBUser
from app.model.user_model import UserModel
from app.repository.auxiliary import check_data_id, check_data_username, update_data, check_data_user
from app.core.extensions import db
from sqlalchemy.exc import SQLAlchemyError
import bcrypt

class AddUser(AddDBUser):
    def add_db(self, hash : HashingDB, check : CheckDB, obj : UserModel):
        try:
            ch = check.check_by_username(username=obj.username, email=obj.email)

            if ch != True:
                raise Exception('This user already exists')

            obj.password = hash.hash_password(obj.password)

            db.session.add(obj)
            db.session.commit()

            return obj
        except SQLAlchemyError as e:
            raise SQLAlchemyError(str(e))

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
            user = check_data_user(model=UserModel, name=name)

            return user
        except SQLAlchemyError as e:
            raise SQLAlchemyError(str(e))

class HashingPassword(HashingDB):
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def hash_password_check(self, password, hspassword):
        return bcrypt.checkpw(password.encode(), hspassword)
    
class CheckUser(CheckDB):
    def check_by_username(self, username, email):
        try:
            user = check_data_username(model=UserModel, name=username, email=email)

            return user
        except Exception as e:
            raise Exception(str(e))

class UpdatePasswordUser(UpdateDB):
    def update_db(self, id, obj):
        try:
            user = check_data_id(model=UserModel, id=id)

            res = update_data(model=user, obj=obj)

            db.session.commit()

            return res
        except SQLAlchemyError as e:
            raise SQLAlchemyError(str(e))