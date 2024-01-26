#!/usr/bin/python3
"""script that takes my github credentials"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    douz = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get('https://api.github.com/user', auth=douz)
    print(res.json().get("id"))
