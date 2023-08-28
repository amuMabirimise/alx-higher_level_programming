#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if isinstance(element, int):
                if count < x:
                    formatted_value = "{:d}".format(element)
                    print(formatted_value, end=' ')
                    count += 1
                else:
                    break
        print()
        return count
    except:
        return count

