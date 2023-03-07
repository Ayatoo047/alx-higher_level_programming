#!/usr/bin/python3
for i in range(0, 100):
    i = (f'0{i},') if i < 10 else (f'{i},')
    if i != '99,':
        print(i, end = ' ')
    else:
        print(99)
