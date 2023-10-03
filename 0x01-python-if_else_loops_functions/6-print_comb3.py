#!/usr/bin/python3
for a in range(10):
    for h in range(a, 10):
        if a < h:
            print("{:d}{:d}".format(a, h), 
                    end="\n" if a == 8 and h == 9 else ", ")
