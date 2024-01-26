#!/usr/bin/python3
"""
retuns value of variable found in the header of the response
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io") as res:
        me = res.read()
        alo = res.getheader("X-Request-Id")
        print(alo)
