#!/usr/bin/python3

def text_indentation(text):
    """
    Print text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Returns:
        None

    Raises:
        TypeError: If `text` is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.split(".")
    for line in lines:
        questions = line.split("?")
        for question in questions:
            colons = question.split(":")
            for colon in colons:
                print(colon.strip())
            if len(colons) > 1:
                print()
        if len(questions) > 1:
            print()
