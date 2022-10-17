#!/usr/bin/python3
"""
Defining a class rectangle
"""


class Rectangle:
    """ Rectangle representation"""
    def __init__(self, width=0, height=0):
        """Initializing the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter func for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter func for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter func for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter func for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
