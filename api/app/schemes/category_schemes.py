from app.core.extensions import ma
from marshmallow import validate, fields, post_load
from app.model.category_model import CategoryModel


class CategorySchemes(ma.Schema):
    id = fields.Integer(required=True, dump_only=True)
    name_category = fields.String(required=True, validate=validate.Length(min=8, max=256))
    category_description = fields.String(required=True, validate=validate.Length(min=8, max=1024))

    @post_load
    def make_category(self, data, **kwargs):
        return CategoryModel(**data)
