#!/usr/bin/python3
"""Module for the class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from class BaseGeometry"""
    def __init__(self, width, height):
        """a new instance of Rectangle

        Args:
            width: the width of a rectangle
            height: the height of a rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
