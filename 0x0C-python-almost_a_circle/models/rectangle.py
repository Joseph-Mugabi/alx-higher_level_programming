#!/usr/bin/python3
"""
class Rectangle

Inherits from Base
inits superclass' id
contains private instance attributes width, height, x and y
"""


from models.base import Base


class Rectangle(Base):
    """
    defines class Rectangle; inherits from Base
    inherited Attributes:
        id
    Class Attributes:
        __width
        __height
        __x
        __y
    methods:
        __init__(self, width, height, x=0, y=0, id=None):

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the constructor class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= o")
        self.__x = value

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """displays and Print to stdout a rectangle using #'s"""
        print("\n" * self.__y + "\n".join(" " * self.__x + "#" * self.width
                                          for idx in range(self.__height)))

    def __str__(self):
        """print object attributes"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format
        (self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        keys = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                setattr(self, keys[i], arg)
        else:
            for keys in kwargs:
                setattr(self, keys, kwargs[keys])

    def to_dictionary(self):
        """Update the class Rectangle by adding the public method
        that returns the dictionary representation of a Rectangle"""
        return self.__dict__
