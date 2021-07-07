from dataclasses import dataclass

from marshmallow import fields, Schema, EXCLUDE


@dataclass
class AdRequest(object):
    sdk_version: str
    session_id: str
    platform: str
    username: str
    country_code: str


class AdRequestSchema(Schema):
    class Meta:
        index_errors = True
        unknown = EXCLUDE

    sdk_version = fields.String(required=True)
    session_id = fields.String(required=True)
    platform = fields.String(required=True)
    username = fields.String(required=True)
    country_code = fields.String(required=True)
