from flask import request, Response
from flask_restful import Resource

from app.application.flask.helpers.response import make_custom_response
from app.application.services.sdk_service import SDKService
from app.application.services.user_service import UserService
from app.domain.entities.request import RequestSchema


class ImpressionView(Resource):
    request_type = "impression_requests"

    def __init__(self, sdk_service: SDKService, user_service: UserService):
        self.sdk_service = sdk_service
        self.user_service = user_service

    @make_custom_response
    def get(self):
        ad_request = RequestSchema().load(request.args)
        self.sdk_service.increment(
            ad_request.get('sdk_version'), self.request_type)
        self.user_service.increment(
            ad_request.get('username'), self.request_type)
        return Response(status=200)
