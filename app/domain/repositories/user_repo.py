from abc import abstractmethod
from typing import Optional

from app.domain.entities.user import User
from app.domain.repositories import BaseRepo


class UserBaseRepo(BaseRepo):
    @abstractmethod
    def create(self, user: User) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def get_avg_impressions(self):
        raise NotImplementedError

    @abstractmethod
    def get_avg_ad_requests(self):
        raise NotImplementedError

    @abstractmethod
    def increment_request(self, username: str, request_type: str):
        raise NotImplementedError
