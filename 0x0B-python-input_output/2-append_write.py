#!/usr/bin/python3
"""Defines a function for appending text to a file."""

def append_write(filename="", text=""):
    """Adds a string to the end of a UTF8-encoded text file.

    Args:
        filename (str): The file to which the text will be appended.
        text (str): The text to be added to the file.
    Returns:
        An integer representing the count of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)

