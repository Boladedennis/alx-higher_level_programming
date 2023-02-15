#!/usr/bin/python3
"""
Print a square with character #
size is the length of the square
"""

def print_square(size):
    """
    args: size is the length of the square
    size must be an integer otherwise it raises a TypeError
    """
    if size < 0:
        raise ValueError('size must be >=0')
    elif not isinstance(size, int):
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
