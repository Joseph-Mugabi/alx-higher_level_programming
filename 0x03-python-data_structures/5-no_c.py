#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            new_string += c
    return new_string

# alternatively
# def no_c(my_string):
#   return ("".join(c for c in my_string if c not in "Cc"))
