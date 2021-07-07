from app.domain.entities.sdk import SDK
from app.domain.repositories.sdk_repo import SDKBaseRepo


class SDKService(object):
    def __init__(self, repo: SDKBaseRepo):
        self.repo = repo

    def create(self, sdk: SDK):
        return self.repo.create(sdk)

    def increment(self, sdk_version, request_type):
        return self.repo.increment_request(sdk_version, request_type)

    def avg_impressions(self):
        return self.repo.get_avg_impressions()

    def avg_ad_requests(self):
        return self.repo.get_avg_ad_requests()
