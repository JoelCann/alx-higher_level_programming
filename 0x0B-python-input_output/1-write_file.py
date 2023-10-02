#!/usr/bin/python3
"""Module for the  write_file method"""


def write_file(filename="", text=""):
    """
    a Method that writes strings to text files (UTF8)
    and returns the number of characters it contains
    """
    with open(filename, mode="w", encoding="utf-8") as my_file_3:
        return my_file_3.write(text)
