#!/usr/bin/python3
"""send http request n display value of variable X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    alo = response.headers.get("X-Request-Id")
    print(alo)
