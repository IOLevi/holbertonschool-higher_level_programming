#!/usr/bin/python3
# sends a request to the URL and displays the value 
# of the variable X-Request-Id in the response header

import requests
import sys

if __name__ == "__main__":
    target = sys.argv[1]
    r = requests.get(target)
    a = r.headers['X-Request-Id']
    print(a)