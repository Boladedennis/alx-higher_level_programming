#!/usr/bin/python3
"""
Checks if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ check whether an object is the smae type to the class """
    if type(obj) is a_class:
        return True
    else:
        return False
