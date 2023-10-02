#!/usr/bin/python3
"""a Module for the class student"""


class Student:
    """This Class defines a student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary"""
        return self.__dict__.copy()
