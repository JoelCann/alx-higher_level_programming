#!/usr/bin/python3
"""Module for the number_of_lines method"""


def number_of_lines(filename=""):
    """a Method that returns the n0. of lines of in text file"""
    with open(filename, encoding="utf-8") as my_file_0:
        lineNum = 0
        while True:
            line = my_file_0.readline()
            if not line:
                break
            lineNum += 1
    return lineNum
