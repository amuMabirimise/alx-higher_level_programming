#!/usr/bin/python3

def swap(a, b):
    # Your code here (line 4)
    a, b = b, a
    return a, b


# Test the function
a = 5
b = 10
a, b = swap(a, b)
print("a =", a)  # Output: a = 10
print("b =", b)  # Output: b = 5
