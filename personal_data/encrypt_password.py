#!/usr/bin/env python3
"""Password hasher and checker using bcrypt"""

import bcrypt


def create_hashed_password(user_password: str) -> bytes:
    """Takes a plain password and returns a hashed version"""
    return bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())


def check_password_match(hashed_pass: bytes, plain_pass: str) -> bool:
    """Returns True if the password matches the hashed password"""
    return bcrypt.checkpw(plain_pass.encode(), hashed_pass)