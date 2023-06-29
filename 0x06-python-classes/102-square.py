#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(the_square, size=0):
        """Initializes a new square.
        Args:
            size (int): The length of the new square.
        """
        the_square.size = size

    @property
    def size(the_square):
        """Gets the current size of the square."""
        return (the_square.__size)

    @size.setter
    def size(the_square, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        the_square.__size = value

    def area(the_square):
        """Returns the current area of the square."""
        return (the_square.__size * the_square.__size)

    def __eq__(the_square, other):
        """Defines the == comparision to a Square."""
        return the_square.area() == other.area()

    def __ne__(the_square, other):
        """Defines the != comparison to a Square."""
        return the_square.area() != other.area()

    def __lt__(the_square, other):
        """Defines the < comparison to a Square."""
        return the_square.area() < other.area()

    def __le__(thse_square, other):
        """Define the <= comparison to a Square."""
        return the_square.area() <= other.area()

    def __gt__(the_square, other):
        """Defines the > comparison to a Square."""
        return the_square.area() > other.area()

    def __ge__(the_square, other):
        """Defines the >= compmarison to a Square."""
        return the_square.area() >= other.area()
