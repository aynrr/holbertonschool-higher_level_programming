#!/usr/bin/python3
""" a comment"""


class Student:
    """at first we create a class"""
    def __init__(self, first_name, last_name, age):
        """creating public instance attr."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the dict."""
        return self.__dict__
