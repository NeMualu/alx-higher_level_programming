#!/usr/bin/python3
def simple_delete(a_dict, k=""):
    if k in a_dict:
        del a_dict[k]
    return a_dict
