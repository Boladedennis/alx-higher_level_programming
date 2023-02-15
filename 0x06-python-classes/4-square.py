#!/usr/bin/python3
"""Define a class sqaure"""


class Square:
    """Class square with private attribute instance"""
    def __init__(self, size=0):
        """Initialize a new square with the size argument"""
        self.__size = size

    def area(self):
        """Return the current square area"""
        return(self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
