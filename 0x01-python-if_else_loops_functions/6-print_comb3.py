#!/usr/bin/python3
for a in range(0, 10):
    if a == 8:
        break
    for h in range(a, 10):
        if h == a:
            continue
        print('{}{}'.format(a, h), end=", ")
    print('{}{}'.format(a, h))
