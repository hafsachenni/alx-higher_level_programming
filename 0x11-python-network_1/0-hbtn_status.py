#!/usr/bin/python3

import urllib.request
if __name__ == "__main__":
    response = urllib.request.urlopen("https://alx-intranet.hbtn.io/status")
    me = response.read()
    print(me)
