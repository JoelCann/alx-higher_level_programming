#!/usr/bin/python3
"""Module for the add_Attribute method"""


def add_attribute(obj, name, value):
    """a Method that tests if an attribute can be added"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
