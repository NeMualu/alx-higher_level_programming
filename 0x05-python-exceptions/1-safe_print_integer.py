#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer using "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        True if the printing is successful, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

