from sqlalchemy.orm import Session


class BaseSQLLightRepoError(Exception):
    pass


class SQLLightBaseRepo(object):
    def __init__(self, session: Session):
        self.session: Session = session

    @staticmethod
    def commit_action(fn):
        def wrapped(self, *args, **kwargs):
            result = fn(self, *args, **kwargs)
            self.session.commit()
            return result

        return wrapped
