#!/usr/bin/python3
"""Module for the function inherits_from"""


def inherits_from(obj, a_class):
    """
    this function returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class and false if not.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
