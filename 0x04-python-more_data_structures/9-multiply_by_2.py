#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for i in a_dictionary:
        new.update({i: (a_dictionary.get(i) * 2)})
    return new
