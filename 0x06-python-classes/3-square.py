#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): length of a side of the square
    """
    def __init__(the_square, size=0):
        """initializing square
        Args:
            size (int): length of a side of the square
        Returns:
            Nothing
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                the_square.__size = size

    def area(the_square):
        """computes the area of a square.
        Returns:
            area of square
        """
        return (the_square.__size) ** 2
