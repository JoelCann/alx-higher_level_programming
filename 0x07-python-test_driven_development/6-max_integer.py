#!/usr/bin/python3
"""Module that finds the maximum integer in a list
"""


def max_integer(list=[]):
    """a Function that finds and returns the maximum integer in a list of integers
        If list is empty, function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    a = 1
    while a < len(list):
        if list[a] > result:
            result = list[a]
        a += 1
    return result
