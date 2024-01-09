#!/usr/bin/python3
"""Module to handle writing objects to a file in JSON format."""
import json

def save_to_json_file(my_obj, filename):
    """Saves a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to be saved.
        filename: The name of the file where the object will be stored.

    This function writes the JSON representation of my_obj to filename.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)

