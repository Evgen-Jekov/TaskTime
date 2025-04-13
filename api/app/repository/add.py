from app.repository.database_abc import AddDB
from app.core.extensions import db
from sqlalchemy.exc import SQLAlchemyError

class AddEssence(AddDB):
    def add_db(self, object):
        try:
            db.session.add(object)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise SQLAlchemyError