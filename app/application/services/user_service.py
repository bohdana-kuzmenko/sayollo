from app.domain.entities.user import User
from app.domain.repositories.user_repo import UserBaseRepo


class UserService(object):
    def __init__(self, repo: UserBaseRepo):
        self.repo = repo

    def create(self, user: User):
        return self.repo.create(user)

    def increment(self, username, request_type):
        return self.repo.increment_request(username, request_type)

    def avg_impressions(self):
        return self.repo.get_avg_impressions()

    def avg_ad_requests(self):
        return self.repo.get_avg_ad_requests()
