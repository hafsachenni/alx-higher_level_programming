#!/usr/bin/python3
"""post requets with letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    value = {'q': letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        j = response.json()
        if j == {}:
            print("No result")
        else:
            print("[{}] {}".format(j.get('id'), j.get('name')))
    except ValueError:
        print("Not a valid JSON")
