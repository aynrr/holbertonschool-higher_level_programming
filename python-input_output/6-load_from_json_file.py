#!/usr/bin/python3
"""a function that creates object from json file"""
import json


def load_from_json_file(filename):
    """at first we open it in read mode"""
    with open(filename, "r", encoding="utf-8") as file:
        """then we change the format from json"""
        return json.load(file)
