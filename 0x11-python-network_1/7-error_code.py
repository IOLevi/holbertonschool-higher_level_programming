#!/usr/bin/python3
# sends a request to the URL and displays the body of the response.

import requests
import sys

if __name__ == "__main__":
    target = sys.argv[1]
    r = requests.get(target)
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(r.status_code))
