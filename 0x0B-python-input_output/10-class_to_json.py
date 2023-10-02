#!/usr/bin/python3
"""a Module for the  class_to_json method"""


def class_to_json(obj):
    """
    a Method that returns the dictionary description
    with simple data structure for SON serialization of an object
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    else:
        return {}
