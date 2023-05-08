#!/usr/bin/python3
"""Define a square based on 2-square.py"""


class Square:
    """class square with private attribute instance, size"""
    def __init__(self, size=0):
        """Initialize new square with size argument"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Return area"""
        return self.__size * self.__size
