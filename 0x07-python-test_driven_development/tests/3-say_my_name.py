#!/usr/bin/python3
"""Module for a function that prints a full name."""


def say_my_name(first_name, last_name=""):
    """Display a full name.

    Args:
        first_name (str): The given first name.
        last_name (str, optional): The given last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name are not string types.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

