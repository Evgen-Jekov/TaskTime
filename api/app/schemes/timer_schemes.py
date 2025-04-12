from app.core.extensions import ma
from marshmallow import fields


class TimerSchemes(ma.Schema):
    id = fields.Integer(required=True, dump_only=True)
    start_time = fields.DateTime(required=True, format='%Y-%m-%dT%H:%M:%S')
    end_time = fields.Date(required=True, format='%Y-%m-%dT%H:%M:%S')
    general_hours = fields.Float(required=True)