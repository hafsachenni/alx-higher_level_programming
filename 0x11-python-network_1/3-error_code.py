#!/usr/bin/python3
"""sending request and displaying body of the response"""

import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
        alo = res.read().decode("utf-8")
        print(alo)
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
