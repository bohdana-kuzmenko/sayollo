from app.application.flask.run import FlaskAPIRunner
from app.application.services.sdk_service import SDKService
from app.application.services.user_service import UserService
from app.infrastructure.repositories.sqllight.sdk_repo import \
    SDKRepo
from app.infrastructure.repositories.sqllight.user_repo import \
    UserRepo
from app.infrastructure.repositories.sqllight import session, create_tables


def main():
    create_tables()
    sqllight_repo = SDKRepo(session)
    sdk_service = SDKService(sqllight_repo)

    user_repo = UserRepo(session)
    user_service = UserService(user_repo)
    FlaskAPIRunner(sdk_service, user_service).run()


if __name__ == '__main__':
    main()
