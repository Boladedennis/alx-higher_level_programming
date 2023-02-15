#!/usr/bin/python3
"""class square that defines a square by 1-square.py"""


class Square:
    """class Square with private instance atribute size"""
    def __init__(self, size=0):
        """initialize new square with size argument"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
