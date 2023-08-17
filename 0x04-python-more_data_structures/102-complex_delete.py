#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_to_delete = []
    keys = list(a_dictionary.keys())
    index = 0

    while index < len(keys):
        key = keys[index]
        if a_dictionary[key] == value:
            keys_to_delete.append(key)
        index += 1

    for key in keys_to_delete:
        del a_dictionary[key]
