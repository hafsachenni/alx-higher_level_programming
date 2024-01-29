#!/usr/bin/python3
"""script that sends a post request"""
import requests
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(sys.argv[1], payload)
    print(response.text)
