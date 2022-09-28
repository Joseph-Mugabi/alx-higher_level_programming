#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        sum_prodct = 0
        weights = 0
        for tup in my_list:
            sum_prodct += (tup[0] * tup[1])
            weights += tup[1]
        return (sum_prodct / weights)
    return (0)
