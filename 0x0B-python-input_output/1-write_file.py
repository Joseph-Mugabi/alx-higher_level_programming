#!/usr/bin/python3
"""
Module 1-write_file

contain function that writes text file and returns number chars written
"""


def write_file(filename="", text=""):
    """writes to text file and returns number chars written """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
