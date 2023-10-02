#!/usr/bin/python3
"""Module for the from_json_string method"""
import json


def from_json_string(my_str):
    """
    a method that returns an object
    represented by a JSON string
    """
    return json.loads(my_str)
