#!/usr/bin/python3
"""Writing a lookup function."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
