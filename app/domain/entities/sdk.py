from dataclasses import dataclass
from typing import Optional


@dataclass
class SDK(object):
    sdk_version: str
    ad_requests: Optional[int] = 0
    impression_requests: Optional[int] = 0
