#!/usr/bin/python3
def complex_delete(a_dict, value):
    k_to_del = [k for key, val in a_dict.items() if val == value]
    for k in k_to_del:
        del a_dict[k]
    return a_dict

