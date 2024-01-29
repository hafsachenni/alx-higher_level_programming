#!/usr/bin/python3
"""script that sends a post request"""
import requests
import sys


if __name__ == "__main__":
    email = {'alo': 'chkoun'}
    response = requests.post(sys.argv[1], data=email)
    alo = response.text
    print(alo)
    print("Your email is: ", email)

