#!/usr/bin/python3
"""writing a file"""


def write_file(filename="", text=""):
    """opening in write mode and writing the text"""
    with open(filename, "w", encoding="utf-8") as file:
        print(file.write(text))
