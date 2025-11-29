#!/usr/bin/python3
"""rectangle class inheriting from BaseGeometry"""

class Rectangle(BaseGeometry):
    """rectangle with width and height"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__geight = height
