#!/usr/bin/env python3
""" Module of Auth
"""
from flask import request

class Auth:
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """To be used Later"""
        return False
    
    
    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        return None
    
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user"""
        Return None