#!/usr/bin/python3
'''fetch data from header'''


if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    request = requests.get(url)
    header_file = request.headers.get('X-Request-Id')
    print(header_file)
