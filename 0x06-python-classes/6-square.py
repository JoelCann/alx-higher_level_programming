#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """ a square
    Attributes:
        __size (int): length of a size of the square
        __position (tuple): position of the square in 2D dimention
    """
    def __init__(the_square, size=0, position=(0, 0)):
        """initializing the square
        Args:
            size (int): length of a side of the square
            position (tuple): positoin of the square in 2D dimention
        Returns:
            Nothing
        """
        the_square.size = size
        the_square.position = position

    def area(the_square):
        """calculating the square's area
        Returns:
            area of the square
        """
        return (self.__size) ** 2

    @property
    def size(the_square):
        """getting of __size
        Returns:
            size of the square
        """
        return the_square.__size

    @size.setter
    def size(the_square, value):
        """setting of __size
        Args:
            value (int): length of a side of the square
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

    def my_print(the_square):
        """prints the square
        Returns:
            Nothing
        """
        if the_square.__size == 0:
            print()
            return
        for i in range(the_square.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))

    @property
    def position(self):
        """getting of __position
        Returns:
            position of the square in 2D space
        """
        return the_square.__position

    @position.setter
    def position(the_square, value):
        """setting of __position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            the_square.__position = value
