#!/usr/bin/python3
"""
python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    response = urllib.request.urlopen("https://alx-intranet.hbtn.io/status")
    me = response.read()
    print('Body Response:')
    print("\t- type: {}".format(type(me)))
    print('\t- content: {}'.format(me))
    print('\t- utf8 content: {}'.format(me.decode("utf-8")))
