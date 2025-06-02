#!/usr/bin/env python3
"""Flask app for Basic Authentication API."""

#!/usr/bin/env python3
"""
Handles authentication logic
"""
import uuid
from user_authentication_service.user import User
from user_authentication_service.db import DB
import bcrypt
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Authentication system"""

    def __init__(self):
        self._db = DB()

    def valid_login(self, email: str, password: str) -> bool:
        """Check if login credentials are valid"""
        user = self._db.find_user_by_email(email)
        if user and user.check_password(password):
            return True
        return False

    def create_session(self, email: str) -> str:
        """Create and store session ID for the user"""
        user = self._db.find_user_by_email(email)
        session_id = str(uuid.uuid4())
        user.session_id = session_id
        self._db.update_user(user.id, session_id=session_id)
        return session_id
