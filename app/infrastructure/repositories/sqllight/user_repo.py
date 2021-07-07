from sqlalchemy import Column, String, Integer, func

from app.domain.entities.user import User
from app.domain.repositories.user_repo import UserBaseRepo
from app.infrastructure.repositories.sqllight.base_repo import (
    SQLLightBaseRepo, BaseSQLLightRepoError)
from app.infrastructure.repositories.sqllight import Base


class UserDTO(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, nullable=False, index=True)
    ad_requests = Column(Integer, nullable=False, default=0)
    impression_requests = Column(Integer, nullable=False, default=0)

    def to_entity(self) -> User:
        return User(
            username=self.username,
            ad_requests=self.ad_requests,
            impression_requests=self.impression_requests
        )

    @staticmethod
    def from_entity(user: User) -> "UserDTO":
        return UserDTO(
            username=user.username,
            ad_requests=user.ad_requests,
            impression_requests=user.impression_requests,
        )

    def __repr__(self):
        return '<User %r>' % self.username


class UserRepo(UserBaseRepo, SQLLightBaseRepo):
    request_types = ('ad_requests', 'impression_requests')

    @SQLLightBaseRepo.commit_action
    def create(self, user: User):
        user_dto = UserDTO.from_entity(user)
        self.session.add(user_dto)

    def get_avg_impressions(self):
        return UserDTO.query.with_entities(
            func.avg(UserDTO.impression_requests).label('avg')).first().avg

    def get_avg_ad_requests(self):
        return UserDTO.query.with_entities(
            func.avg(UserDTO.ad_requests).label('avg')).first().avg

    @SQLLightBaseRepo.commit_action
    def increment_request(self, username: str, request_type: str):
        if request_type not in UserRepo.request_types:
            raise BaseSQLLightRepoError('unsupported request type')
        user = UserDTO.query.filter_by(username=username).first()
        if user:
            setattr(user, request_type, getattr(UserDTO, request_type) + 1)
        else:    
            self.create(User(**{"username": username, request_type: 1}))
