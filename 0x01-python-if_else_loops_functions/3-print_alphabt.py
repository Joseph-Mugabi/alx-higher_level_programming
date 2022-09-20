#!/usr/bin/python3
for b in range(ord('a'), ord('z') + 1):
    if chr(b) != 'e' and chr(b) != 'q':
        print("{:c}".format(b), end='')
