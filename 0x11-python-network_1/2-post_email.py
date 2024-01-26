#!/usr/bin/python3
"""bash script that sends a POST request"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    with urllib.request.Request(url, data) as res:
        print(res.read())
