#!/usr/bin/python3
"""writing a function that writes in json format"""
import json


def save_to_json_file(my_obj, filename):
    """at first we opening it"""
    with open(filename, "w", encoding="utf-8") as file:
        return json.dumps(my_obj, file)
