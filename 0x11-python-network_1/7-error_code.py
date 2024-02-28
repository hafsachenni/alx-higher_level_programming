#!/usr/bin/python3
"""bash script that dispalys body of response"""
import requests
import sys


if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as chaditak:
        print("Error code:", chaditak.response.status_code)
        