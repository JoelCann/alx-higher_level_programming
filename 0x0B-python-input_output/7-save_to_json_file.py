#!/usr/bin/python3
"""Module for the save_to_json_file method"""
import json


def save_to_json_file(my_obj, filename):
    """
    a Method that writes an Object to a
    text file using a JSON representation
    """
    with open(filename, "w") as write_file:
        json.dump(my_obj, write_file)
