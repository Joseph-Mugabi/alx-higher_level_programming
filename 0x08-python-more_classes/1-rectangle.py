#!/usr/bin/python3
"""
Defining a class rectangle
"""


class Rectangle:
    """ rectangle representation"""
    def __init__(self, width=0, height=0):
        """initializing the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter func for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter func for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """getter func for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter func for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
