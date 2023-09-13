#!/usr/bin/python3
"""defines a function"""


def append_write(filename="", text=""):
    """refers to the append write function"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
