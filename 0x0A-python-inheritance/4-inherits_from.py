#!/usr/bin/python3
"""Defines a function to determine inherited class types."""

def inherits_from(obj, a_class):
    """Verify if an object is a derived instance of a specific class.

    Args:
        obj (any): The object to be evaluated.
        a_class (type): The class to compare against the inheritance of obj.
    Returns:
        bool: True if obj is a derived instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

