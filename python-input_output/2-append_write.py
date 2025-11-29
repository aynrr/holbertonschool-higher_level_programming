#!/usr/bin/python3
"""Appending text to a file"""


def append_write(filename="", text=""):
    """opening our file in append mode"""
    with open(filename, "a", encoding="utf-8") as file:
        """then we append the text"""
        return file.write(text)
