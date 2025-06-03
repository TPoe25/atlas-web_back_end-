#!/usr/bin/env python3
"""
Database management for user authentication service.
"""

import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth is a class that handles user authentication operations,"""
    def __init__(self):
        """Initialize the Auth class with a database instance."""
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hash a password using bcrypt."""
        return bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with an email and password."""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = self._hash_password(password)
            return self._db.add_user(email, hashed)

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user login credentials."""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password
            )
        except Exception:
            return False

    def _generate_uuid(self) -> str:
        """Generate a new UUID."""
        return str(uuid.uuid4())

    def create_session(self, email: str) -> str:
        """Create a new session for a user identified by their email."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = self._generate_uuid()
            self._db.update_user(
                user.id,
                session_id=session_id
            )
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Retrieve a user by their session ID."""
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy the session for a user by their user ID."""
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token for user identified by email."""
        try:
            user = self._db.find_user_by(email=email)
            token = self._generate_uuid()
            self._db.update_user(
                user.id,
                reset_token=token
            )
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the password for a user using a reset token."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed = self._hash_password(password)
            self._db.update_user(
                user.id,
                hashed_password=hashed,
                reset_token=None
            )
        except NoResultFound:
            raise ValueError("Invalid reset token")
