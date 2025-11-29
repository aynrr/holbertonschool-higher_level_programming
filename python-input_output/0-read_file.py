#!/usr/bin/python3
"""creating a function that prints a text file"""


def read_file(filename=""):
    """we open it with "with" and ind read mode"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end = "")
