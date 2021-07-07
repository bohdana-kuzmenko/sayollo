from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URL = "sqlite:///foo.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False, },
)
session = scoped_session(sessionmaker(
    bind=engine, autocommit=False, autoflush=False))
Base = declarative_base()
Base.query = session.query_property()


def create_tables():
    Base.metadata.create_all(bind=engine)
