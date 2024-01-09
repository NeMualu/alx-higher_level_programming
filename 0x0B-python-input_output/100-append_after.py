#!/usr/bin/python3
"""Defines a text file insertion function."""

def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    updated_text = ""
    with open(filename) as reader:
        for line in reader:
            updated_text += line
            if search_string in line:
                updated_text += new_string
    with open(filename, "w") as writer:
        writer.write(updated_text)

