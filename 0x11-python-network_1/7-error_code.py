#!/usr/bin/python3
'''script that print status code'''


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    request = requests.get(url)
    if request.status_code >= 400:
        print('Error code: {}'.format(request.status_code))
    else:
        print(request.text)
