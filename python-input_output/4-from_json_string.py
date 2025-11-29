#!/usr/bin/python3
"""A function that changes format from json to dict"""
import json


def from_json_string(my_str):
    """we use loads for changing format"""
    return json.loads(my_str)
