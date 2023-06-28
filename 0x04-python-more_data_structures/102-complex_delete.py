#!/usr/bin/python3
def complex_delete(the_dict, value):
    keys_del = []
    for key in the_dict:
        if the_dict[key] == value:
            keys_del.append(key)
    for key in keys_del:
        del the_dict[key]
    return the_dict
