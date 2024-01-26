#!/usr/bin/python3
"""post requets with letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        q = ""
    else:
        q = sys.argv[1]
    value = {'q': letter}
    response = requets.post(sys.argv[1], data=value)
    try:
        j = response.json()
        if j == {}:
            print("No result")
        else:
            print("[{}] {}".format(j.get(id), j.get(name)))
    except ValueError:
        print("Not a valid JSON")
