#!/usr/bin/env python3
"""
Definition of class BasicAuth
"""
import base64
from .auth import Auth
from typing import TypeVar

from models.user import User


class BasicAuth(Auth):
    """ Implement Basic Authorization protocol methods
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """base64 authorization_header extractor"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        token = authorization_header.split(" ")[-1]
        return token
