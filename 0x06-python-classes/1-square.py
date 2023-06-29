#!/usr/bin/python3
"""definition for a square class"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(the_square, size):
        """Initializes a square
        Args:
            size (int): length of a side
        Returns: nothing
        """
        the_square.__size = size
