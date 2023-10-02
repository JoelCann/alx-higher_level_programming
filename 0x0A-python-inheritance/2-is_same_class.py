#!/usr/bin/python3
"""Module for the function is_same_class"""


def is_same_class(obj, a_class):
    """
    this function returns True if the object is an instance
    of the specified class, otherwise False.
    """
    return type(obj) is a_class
