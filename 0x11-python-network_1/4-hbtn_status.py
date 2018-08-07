#!/usr/bin/python3
# Write a Python script that fetches https://intranet.hbtn.io/status

import requests

if __name__ == "__main__":
    target = 'https://intranet.hbtn.io/status'
    r = requests.get(target)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))