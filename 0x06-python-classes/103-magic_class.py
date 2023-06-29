#!/usr/bin/python3
"""Defines a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """a circle."""

    def __init__(the_square, radius=0):
        """Initializes a MagicClass.
        Arg:
            radius (float or int):radius of the new MagicClass.
        """
        the_square.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        the_square.__radius = radius

    def area(the_square):
        """Returns the area of the MagicClass."""
        return (the_square.__radius ** 2 * math.pi)

    def circumference(the_square):
        """Returns The circumference of the MagicClass."""
        return (2 * math.pi * the_square.__radius)
