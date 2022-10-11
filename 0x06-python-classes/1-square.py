#!/usr/bin/python3
""" Square class definition for module square """


class Square:
    """
    class Square definition

    Args:
        size : size of a side in square
    """
    def __init__(self, size):
        """
        Initializes square

        Attributes:
            size: size of a side of square
        """
        self.__size = size
