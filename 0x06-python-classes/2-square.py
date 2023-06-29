#!/usr/bin/python3
"""defining the class Square"""


class Square:
    """ the square
    Attributes:
        __size (int): length of a side of the square
    """
    def __init__(the_square, size=0):
        """initializing square
        Args:
            size (int): length of side of the square
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
