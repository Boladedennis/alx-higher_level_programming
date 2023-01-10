#!/usr/bin/python3
""" function that writes from text file
"""


def write_file(filename="", text=""):
    """
    returns the number of characters that are written
    Args:
        filename(str) : name of the file
        text(str): text to write
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
