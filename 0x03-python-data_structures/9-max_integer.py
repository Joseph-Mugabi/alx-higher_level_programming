#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 1:
        return my_list[0]
    else:
        max = max_integer(my_list[1:])
        return(max if max > my_list[0] else my_list[0])
