#!/usr/bin/python3
'''script that authenticate github with
credentials passed'''


if __name__ == '__main__':
    import sys
    import requests
    from requests.auth import AuthBase

    auth = AuthBase(sys.argv[1], sys.argv[2])

    request = requests.get("https://api.github.com/user", auth=auth)
    print(request.json().get('id'))
