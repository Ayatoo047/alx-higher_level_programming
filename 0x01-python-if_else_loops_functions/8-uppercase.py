#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for c in str:
        char = chr(ord(c) - 32) if ord(c) >= ord('a') and ord(c) <= ord('z') else c
        upper += char 
    print("{}".format(upper))
