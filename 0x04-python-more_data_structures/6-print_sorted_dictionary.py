#!/usr/bin/python3
def print_sorted_dictionary(the_dict):
    for key in sorted(the_dict.keys()):
        print("{:s}: {}".format(key, the_dict[key]))
