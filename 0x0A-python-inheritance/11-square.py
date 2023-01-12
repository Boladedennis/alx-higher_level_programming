#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Initiate class square
"""


class Square(Rectangle):
    """
    define a square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        finds are of a square using inheritance of rectangle
        """
        return super().area()

    def __str__(self):
        """Return a string with description """
        return "[Square] {}/{}".format(self.__size, self.__size)
