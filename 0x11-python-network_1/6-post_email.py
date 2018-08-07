#!/usr/bin/python3
# sends a POST request to the passed URL with the
# email as a parameter, and finally displays the body of the response.

import requests
import sys

if __name__ == "__main__":
    target = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(target, data={'email': sys.argv[2]})
    print(r.text)
