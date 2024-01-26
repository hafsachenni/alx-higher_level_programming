#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    alo = response.text
    print("Body response")
    print("\t- type: {}".format(type(alo)))
    print("\t- content: {}".format(alo))
