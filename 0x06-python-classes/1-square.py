#!/usr/bin/python3
"""Defines a class square based on 0-square.py"""


class Square:
    """class quare with private attribute instance, size"""
    def __init__(self, size=0):
        """Intialize new sqaure with size argument"""
        self.__size = size
