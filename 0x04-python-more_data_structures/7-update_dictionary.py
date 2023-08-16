#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

my_dictionary = {'a': 1, 'b': 2, 'c': 3}
update_dictionary(my_dictionary, 'b', 4)
update_dictionary(my_dictionary, 'd', 5)

for key, value in my_dictionary.items():
    print("{}: {}".format(key, value))
