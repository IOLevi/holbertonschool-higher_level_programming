# !/usr/bin/python3
# a Python script that takes in a string and sends 
# a search request to the Star Wars API

import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/?search={}'.format(sys.argv[1]))
    
    try:
        j = r.json()
        print("Number of results: {}".format(j['count']))
        
        for d in j.get('results'):
            print(d['name'])
    except ValueError:
        pass


