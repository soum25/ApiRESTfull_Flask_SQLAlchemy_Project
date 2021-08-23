import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SqlAlchemyEngine:
    @staticmethod
    def _get_db_uri():
        return os.environ.get("DB_URL")

    def __init__(self):
        self.engine = create_engine(self._get_db_uri())
        self.session_maker = sessionmaker(bind=self.engine)

    def session(self):
        return self.session_maker()

    def scoped_session(self, parent_session=None):
        return ScopedSession(self.session_maker, session=parent_session)


class ScopedSession:
    def __init__(self, session_maker, session=None):
        self.session_maker = session_maker
        self.session = session
        self.using_parent_session = session is not None

    def __enter__(self):
        if self.session is None:
            self.session = self.session_maker()
        return self.session

    def __exit__(self, exception_type, exception_value, traceback):
        if not self.using_parent_session:
            self.session.close()


ENGINE = SqlAlchemyEngine()
