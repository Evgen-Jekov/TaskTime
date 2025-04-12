from app.core.extensions import ma
from marshmallow import fields, validate


class TaskSchemes(ma.Schema):
    id = fields.Integer(required=True, dump_only=True)
    name_task = fields.String(required=True, validate=validate.Length(min=8, max=256))
    task_description = fields.String(required=True, validate=validate.Length(min=8, max=1024))
    state_task = fields.String(required=True, validate=[
        validate.Length(min=8, max=32),
        validate.OneOf(['started', 'in progress', 'completed', 'overdue'])
    ])
    deadline = fields.Date(required=True, format='%Y-%m-%d')