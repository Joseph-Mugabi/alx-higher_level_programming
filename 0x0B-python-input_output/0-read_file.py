#!/usr/bin/python3
"""
Read_file function
"""


def read_file(filename=""):
    """reads a text FILE(UTF-8) & prints it to stdout"""
    with open(filename, "r" encoding="utf-8") as f:
        print(f.read(), end="")
