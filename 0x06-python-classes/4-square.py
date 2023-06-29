#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """ a square
    Attributes:
        __size (int): length of a side of the square
    """
    def __init__(the_square, size=0):
        """initializing the square
        Args:
            size (int): length of a side of the square
        Returns:
            Nothing
        """
        the_square.size = size

    def area(the_square):
        """computes the square's area
        Returns:
            area of the square
        """
        return (the_square.__size) ** 2

    @property
    def size(the_square):
        """getter of __size
        Returns:
            The size of the square
        """
        return the_square.__size

    @size.setter
    def size(the_square, value):
        """setting of __size
        Args:
            value (int): length of a size of the square
        Returns:
            Nothing
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                the_square.__size = value
