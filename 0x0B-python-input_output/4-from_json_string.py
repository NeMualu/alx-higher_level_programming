#!/usr/bin/python3
# 6-from_json_string.py
"""Provides a function to convert a JSON string to a Python object."""
import json

def from_json_string(my_str):
    """Converts a JSON string into its corresponding Python object.

    Args:
        my_str (str): A JSON formatted string.

    Returns:
        The Python representation of the data encoded in my_str.
    """
    return json.loads(my_str)

