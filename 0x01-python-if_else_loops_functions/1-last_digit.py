#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    r = number % -10
else:
    r = number % 10
print("Last digit of", number, 'is', r, end=" ")
if r > 5:
    print("and is greater than 5")
elif r == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
