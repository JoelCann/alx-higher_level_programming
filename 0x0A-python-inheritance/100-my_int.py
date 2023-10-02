#!/usr/bin/python3
"""Module for the class MyInt"""


class MyInt(int):
    """class to swap == and !="""
    def __eq__(self, other):
        """Swap == with !=

        Args:
            other: the object be compared

        Returns: True if value and self are same and
                False if otherwise
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Swap != with ==

        Args:
            other: the object to compared

        Returns: False if value and self are unequal
                True if otherwise
        """
        return super().__eq__(other)
