#!/usr/bin/python3

def safe_print_integer(value):
    try:
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        print()
        return True
    except:
        return False

