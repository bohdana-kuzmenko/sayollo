from flask import Flask
from flask_restful import Api

from app.application.flask.views.ad_view import AdView
from app.application.flask.views.impression_view import ImpressionView
from app.application.flask.views.stats_view import StatsView


class FlaskAPIRunner(object):
    def __init__(self, sdk_service, user_service):
        self.sdk_service = sdk_service
        self.user_service = user_service

    def run(self):
        app = Flask(__name__)
        api = Api(app)

        api.add_resource(
            AdView, f'/api/v1/ad',
            resource_class_kwargs={
                'sdk_service': self.sdk_service,
                'user_service': self.user_service,
            })
        api.add_resource(
            ImpressionView, f'/api/v1/impression',
            resource_class_kwargs={
                'sdk_service': self.sdk_service,
                'user_service': self.user_service,
            })
        api.add_resource(
            StatsView, f'/api/v1/stats',
            resource_class_kwargs={
                'sdk_service': self.sdk_service,
                'user_service': self.user_service,
            })

        app.run(port=5001)
