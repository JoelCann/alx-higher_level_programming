#!/usr/bin/python3
"""Module for the class MyList"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        """Method for printing sorted list"""
        print(sorted(self))
