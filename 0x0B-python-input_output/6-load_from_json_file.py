#!/usr/bin/python3
"""Module for converting JSON file content into a Python object."""
import json

def load_from_json_file(filename):
    """Reads from a JSON file and returns the corresponding Python object.

    Args:
        filename: The path to the JSON file to be read.

    Returns:
        A Python object derived from the JSON file content.
    """
    with open(filename) as file:
        return json.load(file)

