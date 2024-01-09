#!/usr/bin/python3
"""Defines a file-writing function."""

def write_to_file(file_name="", content=""):
    """Write a string to a UTF-8 text file.

    Args:
        file_name (str): The name of the file to write.
        content (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(file_name, "w", encoding="utf-8") as file:
        return file.write(content)

