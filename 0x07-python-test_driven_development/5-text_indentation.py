#!/usr/bin/python3
"""
prints 2 new lines of text after . , ?
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in '.:?':
        text = text.replace(i, '{}\n'.format(i))

    for line in text.splitlines():
        print(line.strip())
