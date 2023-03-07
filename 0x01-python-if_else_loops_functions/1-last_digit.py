#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnumber = number % 10
answer = f"Last digit of {number} is {lastnumber}"
if lastnumber > 5:
    print(answer + " and is greater than 5")
elif lastnumber < 6 and lastnumber != 0:
    print(answer + " and is less than 6 and not 0")
elif lastnumber == 0:
    print(answer + " and is 0")
