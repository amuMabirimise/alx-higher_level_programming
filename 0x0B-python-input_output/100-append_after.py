#!/usr/bin/python3
"""Module: append_after"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file
    after each line containing a specific string
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        read_lines = myfile.readlines()

        modified_lines = []
        for line in read_lines:
            modified_lines.append(line)
            if search_string in line:
                modified_lines.append(new_string + "\n")

    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.writelines(modified_lines)
