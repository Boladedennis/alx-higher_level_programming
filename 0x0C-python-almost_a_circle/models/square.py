#!/usr/bin/python3
"""Inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    intialize square definition
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading string method"""
        return ("[Sqaure] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.height))

    @property
    def size(self):
        """getter for width"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Update with args and kwargs """
        attrs = ["id", "size", "x", "y"]
        if args is not None and len(args) != 0:

            for i in range(len(args)):
                if i >= len(attrs):
                    break
                else:
                    setattr(self, attrs[i], args[i])

        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary represantation of a square
        """
        attrs = ["id", "size", "x", "y"]
        values = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(attrs, values))
