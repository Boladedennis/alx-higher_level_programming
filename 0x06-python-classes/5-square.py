#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Class square with private atrribute instance"""
    def __init__(self, size=0):
        """Intialize new square with size argument"""
        self.__size = size

    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                [print("#", end='') for j in range(self.__size)]
                print('')
