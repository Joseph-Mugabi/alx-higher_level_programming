#!/usr/bin/python3
"""Defines a class Square """


class Square: 
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                self.__size = size
