#!/usr/bin/python3
def uppercase(strl):
    upper = ""
    for c in strl:
        char = chr(ord(c) - 32) if ord(c) >= ord('a') and ord(c) <= ord('z') else c
        upper += char 
    return upper
