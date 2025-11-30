#!/usr/bin/python
"""a function that returns dictionary"""


def class_to_json(obj):
    """obj is a class and we use __dict__ to return dict."""
    return obj.__dict__
