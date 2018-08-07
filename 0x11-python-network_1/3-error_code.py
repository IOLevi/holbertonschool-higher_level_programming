#!/usr/bin/python3
# sends a request to 
# the URL and displays the body of the response (decoded in utf-8).

import urllib.request, urllib.parse, urllib.error
import sys

if __name__ == '__main__':
    target = sys.argv[1]
    try:
        with urllib.request.urlopen(target) as response:
            r = response.read()
            print(r.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
            