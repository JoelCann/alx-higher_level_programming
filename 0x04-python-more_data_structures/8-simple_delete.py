#!/usr/bin/python3
def simple_delete(the_dict, key=""):
    if key in the_dict:
        del the_dict[key]
    return the_dict
