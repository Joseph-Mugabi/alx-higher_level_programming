#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for elm in set(my_list):
        add += elm
    return (add)
