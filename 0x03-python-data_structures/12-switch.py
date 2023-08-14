#!/usr/bin/python3

def swap(a, b):
    a, b = b, a
    return a, b


# Test the function
a = 10
b = 89
a, b = swap(a, b)
print("a=" + str(a) + " - b=" + str(b))
