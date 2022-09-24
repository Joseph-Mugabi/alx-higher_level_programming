#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    le = len(argv)
    print("{:d} {:s}{:s}".format(le - 1, "argument" if le <= 2 else
                            "arguments", "." if le == 1 else ":"))
    for number, element in enumerate(argv):
        if number > 0:
            print("{:d}: {:s}".format(number, element))
