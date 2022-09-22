#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    print("{:d} {:s}{:s}".format(length-1, "argument" if length <= 2
        else "arguments", "." if length == 1 else ":"))
    for number, element in enumerate(argv):
        if number > 0:
            print("{:d}: {:s}".format(number, element))
