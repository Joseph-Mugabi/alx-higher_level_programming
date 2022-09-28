#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    if roman_string == "":
        return (0)
    number = 0
    a_dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for j, k in zip(roman_string, roman_string[1:]):
        if j not in a_dictionary.keys():
            return (0)
        elif a_dictionary[j] >= a_dictionary[k]:
            number += a_dictionary[j]
        else:
            number -= a_dictionary[j]
    number += a_dictionary[roman_string[-1]]
    return number
