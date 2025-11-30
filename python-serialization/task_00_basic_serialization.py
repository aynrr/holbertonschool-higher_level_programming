#!/usr/bin/python3
"""a module that serializates and de serializates"""
import json


def serialize_and_save_to_file(data, filename):
    """serializates and saves json file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """loads and deserializates"""
    with open(filename, "r", encodin="utf-8") as file:
        json.load(file)
