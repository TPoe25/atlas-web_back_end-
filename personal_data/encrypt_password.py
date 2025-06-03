#!/usr/bin/env python3
"""
This file has a function to hash passwords.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash the password using bcrypt.

    Args:
        password (str): The plain password to hash.

    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def check_password(hashed_password: bytes, password: str) -> bool:
    """
    Check if a password matches the hashed one.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain password to verify.

    Returns:
        bool: True if it matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if the password matches the hashed password.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
