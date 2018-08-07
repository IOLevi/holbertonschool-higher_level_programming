import urllib.request
# fetches a website using urllib

if __name__ == '__main__':
    target = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(target) as response:
        r = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(r)))
        print('\t - content: {}'.format(r))
        print('\t - utf8 content: {}'.format(r.decode('utf-8')))
