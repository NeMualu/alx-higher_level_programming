#!/usr/bin/python3
"""Defines a text file-reading function."""

def display_file_content(file_name=""):
    """Print the contents of a UTF-8 text file to stdout."""
    with open(file_name, encoding="utf-8") as file:
        print(file.read(), end="")

