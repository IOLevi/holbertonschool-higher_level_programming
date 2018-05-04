#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """prints indented text with newlines stripped out"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    thelen = len(text)
    i = 0
    while i < thelen:
        print(text[i], end="")
        if text[i] in ".:?":
            print()
            print()
            while i + 1 < thelen and text[i + 1] == " ":
                i += 1
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/5-text_indentation.txt")
