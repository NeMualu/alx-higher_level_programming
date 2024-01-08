#!/usr/bin/python3
"""Defines a function to verify class types."""

def is_same_class(obj, a_class):
    """Determine if an object is exactly an instance of a specified class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to compare against obj's type.
    Returns:
        bool: True if obj is exactly an instance of a_class, else False.
    """
    return type(obj) is a_class

