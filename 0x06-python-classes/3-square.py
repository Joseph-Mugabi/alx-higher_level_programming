#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side in square

    methods/functions:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size=0):
        """
        initializes squ

        attributes:
            __size (int): size of a side of square, defaults to 0 if none
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates area of square

        return area
        """
        return (self.__size)**2
