#!/usr/bin/python3
# script that takes url and display the variable in the header

if __name__ == '__name__':
    import urllib.request
    import sys

    url = sys.argv[1]
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get('x-Request-Id'))
