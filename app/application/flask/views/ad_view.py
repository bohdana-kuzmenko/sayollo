from flask import Response, request
from flask_restful import Resource
import requests

from app.application.flask.helpers.response import make_custom_response
from app.application.services.sdk_service import SDKService
from app.application.services.user_service import UserService
from app.domain.entities.request import RequestSchema


class AdView(Resource):
    request_type = "ad_requests"

    def __init__(self, sdk_service: SDKService, user_service: UserService):
        self.sdk_service = sdk_service
        self.user_service = user_service

    @make_custom_response
    def get(self):
        api_url = ('https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/'
                   'prod/ad/vast')
        response = requests.request('get', api_url)
        ad_request = RequestSchema().load(request.args)
        self.sdk_service.increment(
            ad_request.get('sdk_version'), self.request_type)
        self.user_service.increment(
            ad_request.get('username'), self.request_type)
        return Response(response.text, mimetype='text/xml')
