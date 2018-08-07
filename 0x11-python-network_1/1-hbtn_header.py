#!/usr/bin/python3
# sends a request to the URL and displays the value 
# of the X-Request-Id variable found in the header of the response.

import urllib.request
import sys

if __name__ == '__main__':
    target = sys.argv[1]
    with urllib.request.urlopen(target) as response:
        print(response.info()['X-Request-Id'])