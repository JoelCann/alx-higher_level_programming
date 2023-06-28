#!/usr/bin/python3
def uniq_add(my_list=[]):
    addition = 0
    for a in set(my_list):
        addition += a
    return addition
