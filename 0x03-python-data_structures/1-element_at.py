#!/usr/bin/python3
def element_at(my_list, idx):
    l = len(my_list)
    for element in my_list:
        if 0 <= idx > l:
            return (None)
        else:
            return my_list[idx]
