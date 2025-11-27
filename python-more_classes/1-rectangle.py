#!/usr/bin/python3
"""creating a class that defines a rectaangle."""


class Rectangle:
    """creating some methods"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """initializes the rectangle."""
    @property
    def width(self):
        return self.__width
    """retrieves the width of the rectangle."""
    @width.setter
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width<0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """sets the width of the rectangle"""
    @property
    def height(self):
        return self.__height
    """retrieves the height of the rectangle."""
    @height.setter
    def height(self, value):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height<0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """sets the height pf the rectangle"""
