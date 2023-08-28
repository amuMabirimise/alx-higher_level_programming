#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("Exception: Type Error")
    except TypeError as e:
        raise
