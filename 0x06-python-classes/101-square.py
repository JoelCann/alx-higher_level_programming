#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(the_square, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The length of the new square.
            position (int, int): The position of the new square.
        """
        the_square.size = size
        the_square.position = position

    @property
    def size(the_square):
        """claims the current length of the square."""
        return (the_square.__size)

    @size.setter
    def size(the_square, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        the_square.__size = value

    @property
    def position(the_square):
        """Gets the current position of the square."""
        return (the_square.__position)

    @position.setter
    def position(the_square, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        the_square.__position = value

    def area(the_square):
        """Returns the current area of the square."""
        return (the_square.__size * the_square.__size)

    def my_print(the_square):
        """Prints the square with the # character."""
        if the_square.__size == 0:
            print("")
            return

        [print("") for i in range(0, the_square.__position[1])]
        for i in range(0, the_square.__size):
            [print(" ", end="") for j in range(0, the_square.__position[0])]
            [print("#", end="") for k in range(0, the_square.__size)]
            print("")

    def __str__(the_square):
        """Defines the print() representation of a Square."""
        if the_square.__size != 0:
            [print("") for i in range(0, the_square.__position[1])]
        for i in range(0, the_square.__size):
            [print(" ", end="") for j in range(0, the_square.__position[0])]
            [print("#", end="") for k in range(0, the_square.__size)]
            if i != the_square.__size - 1:
                print("")
        return ("")
