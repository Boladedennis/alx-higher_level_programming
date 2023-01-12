#!/usr/bin/python3
"""
Integer validator
"""


class BaseGeometry():
    """
    Initiate public instance
    """
    def area(self):
        raise Exception('area() is not implemented')
    """
    public instance that validates value
    """
    def integer_validator(self, name, value):
        self.__name = name
        self.__value = value
        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        elif value <=0:
            raise ValueError('<name> must be greater than 0')
