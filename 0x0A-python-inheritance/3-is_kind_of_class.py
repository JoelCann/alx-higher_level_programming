#!/usr/bin/python3
"""Module for the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    this function returns True if the object is an instance of,
    a paernt class from, otherwise False.
    """
    return isinstance(obj, a_class)
