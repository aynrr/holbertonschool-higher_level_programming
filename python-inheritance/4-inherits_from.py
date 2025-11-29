#!/usr/bin/python3
"""function shecks if object inherits from a class"""


def inherits_from(obj, a_class):
    """return true if obj is subclass instance of a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
