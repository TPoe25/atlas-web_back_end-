#!/usr/bin/env python3
"""basic authentication module"""

from api.v1.auth.auth import Auth

from typing import Tuple

class BasicAuth(Auth):
    """Basic authentication class that inherits from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the base64 part of the authorization header"""
        if not authorization_header or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1] if " " in authorization_header else None

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decodes the base64 part of the authorization header"""
        if not base64_authorization_header or not isinstance(base64_authorization_header, str):
            return None
        try:
            import base64
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
    
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """Extracts user email and password"""
        if not decoded_base64_authorization_header or not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":", 1))
        return (None, None)
        return tuple(decoded_base64_authorization_header.split(":", 1))
