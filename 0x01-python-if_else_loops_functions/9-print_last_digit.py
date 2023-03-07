#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = int(repr(number)[-1])
    return (lastdigit * -1) if number < 0 else lastdigit
