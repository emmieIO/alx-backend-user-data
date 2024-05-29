#!/usr/bin/env python3

"""
Password Encryption and Validation Module

This module provides functions for hashing passwords using bcrypt and
validating plain-text passwords against hashed passwords.
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Generate a salted and hashed password.

    Args:
        password (str): The plain-text password to be hashed.

    Returns:
        bytes: The salted and hashed password as a byte string.
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a plain-text password against a hashed password.

    Args:
        hashed_password (bytes): The salted and hashed password as a byte string.
        password (str): The plain-text password to be validated.

    Returns:
        bool: True if the provided password matches the hashed password, False otherwise.
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid