# !/usr/bin/python3
# Write a Python script that takes in a letter and
# sends a POST request to http://0.0.0.0:5000/search_user
# with the letter as a parameter.

import requests
import sys

if __name__ == "__main__":

    try:
        target = sys.argv[1]
    except BaseException:
        target = ""
    r = requests.post(
        'http://34.206.234.184:39991/search_user',
        data={
            'q': target})

    try:
        j = r.json()
        if len(j) == 0:
            print("No result")
        else:
            print("[{}] {}".format(j['id'], j['name']))
    except ValueError:
        print("Not a valid JSON")
