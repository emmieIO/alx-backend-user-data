#!/usr/bin/env python3
"""api/v1/auth/basic_auth.py"""


class BasicAuth(Auth):
    """
    Basic Auth Config Class
    """
    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        """
        Extract the Base64 part of the Authorization
        header for Basic Authentication.
        Args:
            authorization_header (str):
            The Authorization header from the request.
        Returns:
            str: The Base64 part of the
            Authorization header or None if invalid.
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]