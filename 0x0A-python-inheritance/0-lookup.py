#!/usr/bin/python3
"""Module for finding attributes of an object."""

def lookup(obj):
    """List all the accessible attributes of a given object.

    Args:
        obj: The object whose attributes need to be listed.

    Returns:
        A list containing the names of the object's attributes.
    """
    return dir(obj)

