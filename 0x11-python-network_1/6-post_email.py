#!/usr/bin/python3
'''requests to make posts'''


if __name__ == '__main__':
    import sys
    import requests

    payload = {'email': sys.argv[2]}
    request = requests.post(sys.argv[1], data=payload)
    print(request.text)
