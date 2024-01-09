#!/usr/bin/python3
"""Module for converting a Python class instance into a JSON-compatible dictionary."""

def class_to_json(obj):
    """Transforms a Python class instance into a dictionary for JSON serialization.

    This function extracts the dictionary representation of a Python class instance,
    typically containing its fields and values, making it suitable for JSON serialization.

    Args:
        obj: The Python class instance to convert.

    Returns:
        A dictionary representation of the class instance.
    """
    return obj.__dict__

