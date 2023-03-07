def print_last_digit(number):
    lastdigit = int(repr(number)[-1])
    if number < 0:
        return lastdigit * -1 else lastdigit
