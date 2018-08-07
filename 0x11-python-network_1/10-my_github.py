#!/usr/bin/python3
# a Python script that takes your Github credentials
# (username and password)
# and uses the Github API to display your id

import requests
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    pword = sys.argv[2]
    r = requests.get(
        'https://api.github.com/users/{}'.format(name),
        auth=requests.auth.HTTPBasicAuth(
            name,
            pword))

    try:
        j = r.json()
        print(j.get('id'))
    except ValueError:
        pass
