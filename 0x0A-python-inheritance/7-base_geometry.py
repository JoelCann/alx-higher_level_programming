#!/usr/bin/python3
"""Module for the class BaseGeometry"""


class BaseGeometry:
    """the class BaseGeometry"""
    def __init__(self):
        """a new instance of BaseGeometry"""
        pass

    def area(self):
        """a Public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a Public instance method that validates value as an int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
