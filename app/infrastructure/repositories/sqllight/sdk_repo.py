from sqlalchemy import Column, String, Integer
from sqlalchemy.sql import func

from app.domain.entities.sdk import SDK
from app.domain.repositories.sdk_repo import SDKBaseRepo
from app.infrastructure.repositories.sqllight.base_repo import (
    SQLLightBaseRepo, BaseSQLLightRepoError)
from app.infrastructure.repositories.sqllight import Base


class SDKDTO(Base):
    __tablename__ = "sdks"
    sdk_version = Column(String, primary_key=True, nullable=False, index=True)
    ad_requests = Column(Integer, nullable=False, default=0)
    impression_requests = Column(Integer, nullable=False, default=0)

    def to_entity(self) -> SDK:
        return SDK(
            sdk_version=self.sdk_version,
            ad_requests=self.ad_requests,
            impression_requests=self.impression_requests,
        )

    @staticmethod
    def from_entity(sdk: SDK) -> "SDKDTO":
        return SDKDTO(
            sdk_version=sdk.sdk_version,
            ad_requests=sdk.ad_requests,
            impression_requests=sdk.impression_requests,
        )

    def __repr__(self):
        return '<SDK %r>' % self.sdk_version


class SDKRepo(SDKBaseRepo, SQLLightBaseRepo):
    request_types = ('ad_requests', 'impression_requests')

    @SQLLightBaseRepo.commit_action
    def create(self, sdk: SDK):
        sdk_dto = SDKDTO.from_entity(sdk)
        self.session.add(sdk_dto)

    def get_avg_impressions(self):
        return SDKDTO.query.with_entities(
            func.avg(SDKDTO.impression_requests).label('avg')).first().avg

    def get_avg_ad_requests(self):
        return SDKDTO.query.with_entities(
            func.avg(SDKDTO.ad_requests).label('avg')).first().avg

    @SQLLightBaseRepo.commit_action
    def increment_request(self, sdk: str, request_type: str):
        if request_type not in SDKRepo.request_types:
            raise BaseSQLLightRepoError('unsupported request type')
        sdk_entity = SDKDTO.query.filter_by(sdk_version=sdk).first()
        if sdk_entity:
            setattr(sdk_entity, request_type,
                    getattr(SDKDTO, request_type) + 1)
        else:
            self.create(SDK(**{"sdk_version": sdk, request_type: 1}))
