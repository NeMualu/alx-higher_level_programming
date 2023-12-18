#!/usr/bin/python3
from __future__ import print_function
import sys

def safe_print_integer_err(value):
    """Prints an integer using "{:d}".format().

    If a ValueError occurs, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        True if the integer is printed successfully, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False

