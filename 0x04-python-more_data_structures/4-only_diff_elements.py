#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = []
    sett3 = set_1.union(set_2)
    for i in sett3:
        if i in set_1 and i in set_2:
            continue
        new.append(i)
    return (new)
