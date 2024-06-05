#!/usr/bin/env python3
""" Module of Auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manages the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Used to protect authenticated routes
           args: path:str, excluded_paths:List[str]
        """
        if path is None:
            return True
        if not excluded_paths:
            return True
        else:
            if not path.endswith('/'):
                path += '/'
            for route in excluded_paths:
                if route.endswith("/") and route == path:
                    return False
            return True

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if request is None:
            return None
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user"""
        return None
