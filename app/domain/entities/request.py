from dataclasses import dataclass

from marshmallow import fields, Schema, EXCLUDE


@dataclass
class Request(object):
    sdk_version: str
    session_id: str
    platform: str
    username: str
    country_code: str


class RequestSchema(Schema):
    class Meta:
        index_errors = True
        unknown = EXCLUDE

    sdk_version = fields.String(required=True)
    session_id = fields.String(required=True)
    platform = fields.String(required=True)
    username = fields.String(required=True)
    country_code = fields.String(required=True)
