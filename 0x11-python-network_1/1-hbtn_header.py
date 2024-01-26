#!/usr/bin/python3
"""
retuns value of variable found in the header of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        me = res.read()
        alo = res.getheader("X-Request-Id")
        print(alo)
