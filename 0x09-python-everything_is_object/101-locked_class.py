#!/usr/bin/python3
"""This module defines a class with restricted attribute assignment."""

class LockedClass:
    """
    This class only allows creating an attribute named 'first_name'.
    Any other attribute creation will not be permitted.
    """

    __slots__ = ['first_name']

