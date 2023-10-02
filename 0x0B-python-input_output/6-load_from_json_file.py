#!/usr/bin/python3
"""a Module for the load_from_json_file method"""
import json


def load_from_json_file(filename):
    """this Method creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="utf-8") as file_load:
        return json.load(file_load)
