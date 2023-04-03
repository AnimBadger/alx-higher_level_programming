#!/usr/bin/python3
'''request module to fetch data'''


if __name__ == '__main__':
    import requests

    data = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(data.text.__class__))
    print('\t- content: {}'.format(data.text))
