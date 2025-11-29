#!/usr/bin/python3
"""A function that returns rhe json format"""
import json


def to_json_string(my_obj):
    """At first we importeed"""
    result = json.dumps(my_obj)
    """then we used dumps for string"""
    return result
