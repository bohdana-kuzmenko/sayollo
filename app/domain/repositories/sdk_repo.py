from abc import abstractmethod
from typing import Optional

from app.domain.entities.sdk import SDK
from app.domain.repositories import BaseRepo


class SDKBaseRepo(BaseRepo):
    @abstractmethod
    def create(self, sdk: SDK) -> Optional[SDK]:
        raise NotImplementedError

    @abstractmethod
    def get_avg_impressions(self):
        raise NotImplementedError

    @abstractmethod
    def get_avg_ad_requests(self):
        raise NotImplementedError

    @abstractmethod
    def increment_request(self, sdk_version: str, request_type: str):
        raise NotImplementedError
