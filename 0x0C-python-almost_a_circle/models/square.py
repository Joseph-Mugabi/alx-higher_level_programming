#!/usr/bin/python3
"""
class Square

inherits from Rectangle;
Inits superclass' id, width (as size), height (as size), x, y
ontains public attribute size
Prints [Square] (<id>) <x>/<y> - <size>
Updates attributes: arg1=id, arg2=size, arg3=x, arg4=y
Returns dictionary representation of attributes
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A representation of a class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """updates class square by adding the public method
        that assigns attributes"""
        keys = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for idx, arg in enumerate(args):
                setattr(self, keys[idx], arg)
        else:
            for keys in kwargs:
                setattr(self, keys, kwargs[keys])

    def to_dictionary(self):
        """Update the class Square by adding the public method
        that returns the dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
