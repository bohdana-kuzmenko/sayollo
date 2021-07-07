from dataclasses import dataclass
from typing import Optional


@dataclass
class User(object):
    username: str
    ad_requests: Optional[int] = 0
    impression_requests: Optional[int] = 0
