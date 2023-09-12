#!/usr/bin/python3

def write_file(filename="", text=""):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_characters_written = file.write(text)
            return num_characters_written
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0
