#!/usr/bin/python3
"""bash script that sends a POST request"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    """encoding the data"""
    data = urllib.parse.urlencode(value).encode("utf-8")
    """request object creation"""
    request = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(request) as res:
        alo = res.read()
        print(alo.decode("utf-8"))
