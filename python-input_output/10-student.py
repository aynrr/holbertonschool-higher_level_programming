#!/usr/bin/python3
""" a comment"""


class Student:
    """at first we create a class"""
    def __init__(self, first_name, last_name, age):
        """creating public instance attr."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves the dict."""
        if isinstance(attrs, list):
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
        return self.__dict__
