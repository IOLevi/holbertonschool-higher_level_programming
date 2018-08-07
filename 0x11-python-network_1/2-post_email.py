#!/usr/bin/python3
# sends a POST request to the passed URL with the email
# as a parameter, and displays the body of the response (decoded in utf-8)

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    target = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('utf-8')
    with urllib.request.urlopen(target, data) as response:
        r = response.read()
        print(r.decode('utf-8'))
