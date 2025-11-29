#!/usr/bin/python3
"""a function that searchs object's instance"""


def is_kind_of_class(obj, a_class):
    """True if obj is instance of a_class/its subclass else False"""
    return isinstance(obj, a_class)
