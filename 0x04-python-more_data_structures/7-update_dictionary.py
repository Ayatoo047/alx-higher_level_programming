#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
   new = a_dictionary.copy()
   new.update({key: value})
   return new
