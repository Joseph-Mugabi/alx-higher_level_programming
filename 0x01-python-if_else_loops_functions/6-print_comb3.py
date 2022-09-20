#!/usr/bin/python3
for j in range(0, 8):
    for k in range((j + 1), 10):
        print("{}{}, ".format(j, k), end='')
print("{}{}".format(j + 1, k))
