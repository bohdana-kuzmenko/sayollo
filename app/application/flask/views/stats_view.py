from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError

from app.application.flask.helpers.response import make_custom_response
from app.application.services.sdk_service import SDKService
from app.application.services.user_service import UserService


class StatsView(Resource):
    def __init__(self, sdk_service: SDKService, user_service: UserService):
        self.sdk_service = sdk_service
        self.user_service = user_service

    @make_custom_response
    def get(self):
        filter_type = request.args.get('filter_type')
        if not filter_type:
            raise ValidationError("No filter type have been provided")
        services = {
            'user': self.user_service,
            'sdk': self.sdk_service,
        }
        if filter_type not in services:
            raise ValidationError("Unrecognized filer type have been provided")
        avg_impressions = services[filter_type].avg_impressions()
        avg_ad_requests = services[filter_type].avg_ad_requests()
        rate = avg_impressions / avg_ad_requests if avg_ad_requests else 0
        return jsonify({
            "avg_impressions": avg_impressions,
            "avg_ad_requests": avg_ad_requests,
            "rate": rate
        })
