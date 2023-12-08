#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element in a new list.

    Args:
        my_list (list): The original list.
        search: The element to replace in the list.
        replace: The new element.

    Returns:
        list: A new list with all occurrences of `search`
        replaced by `replace`.
    """
    return [replace if element == search else element for element in my_list]

