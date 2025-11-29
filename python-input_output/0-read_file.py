#!/usr/bin/python3
"""creating a function that prints a text file"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end = "")
