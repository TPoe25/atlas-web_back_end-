#!/usr/bin/env python3
"""Database management for user authentication service."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """
    DB is a database handler class for managing user authentication data using SQLAlchemy.

    Attributes:
        _engine: SQLAlchemy engine instance connected to a SQLite database.
        __session: SQLAlchemy session instance (lazily initialized).

    Methods:
        add_user(email: str, hashed_password: str) -> User:
            Adds a new user with the specified email and hashed password to the database.

        find_user_by(**kwargs) -> User:
            Finds and returns a user matching the provided keyword arguments.
            Raises InvalidRequestError if no arguments are provided or if the query is invalid.
            Raises NoResultFound if no user matches the criteria.

        update_user(user_id: int, **kwargs) -> None:
            Updates attributes of the user with the given user_id using provided keyword arguments.
            Raises ValueError if an invalid attribute is specified.
    """
    def __init__(self) -> None:
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        if not kwargs:
            raise InvalidRequestError()
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound()
        except Exception:
            raise InvalidRequestError()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)
        self._session.commit()
