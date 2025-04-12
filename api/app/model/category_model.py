from app.core.extensions import db
from sqlalchemy import Column, String, Integer, Text


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, nullable=False)
    name_category = Column(String(256), nullable=False)
    category_description = Column(Text(1024), nullable=False)

    tasks = db.relationship('TaskModel', back_populates='category')