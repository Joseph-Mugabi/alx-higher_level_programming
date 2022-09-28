#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    if roman_string == "":
        return (0)
    number = 0
    a_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for j, k in zip(roman_string, roman_string[1:]):
        if j not in a_dict.keys():
            return (0)
        elif a_dict[j] >= a_dict[k]:
            number += a_dict[j]
        else:
            number -= a_dict[j]
    number += a_dict[roman_string[-1]]
    return number
