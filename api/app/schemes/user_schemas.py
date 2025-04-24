from app.core.extensions import ma
from app.model.user_model import UserModel
from marshmallow import fields, post_load

class UserSchemes(ma.Schema):
    id = fields.Integer(required=True, dump_only=True)
    username = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True, load_only=True)

    @post_load
    def make_user(self, data, **kwargs):
        return UserModel(**data)