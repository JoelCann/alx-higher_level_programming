#!/usr/bin/python3
"""Module for the class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from class BaseGeometry"""
    def __init__(self, width, height):
        """new instance of Rectangle

        Args:
            width: the width of a rectangle
            height: the height of a rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """computing the area method"""
        return self.__width * self.__height

    def __str__(self):
        """computing the area method"""
        return "[{}] {:d}/{:d}".format(Rectangle.__name__, self.__width,
                                       self.__height)
