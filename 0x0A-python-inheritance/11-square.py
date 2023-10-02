#!/usr/bin/python3
"""Module for the class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class named Square that inherits from Rectangle"""
    def __init__(self, size):
        """a new instance of class Rectangle

        Args:
            size: the size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[{}] {:d}/{:d}".format(self.__class__.__name__,
                                       self.__size,
                                       self.__size)
