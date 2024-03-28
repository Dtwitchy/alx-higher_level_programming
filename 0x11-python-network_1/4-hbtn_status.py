#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    print('Response Body:')
    print('\t- Type:', type(response.content.decode()))
    print('\t- Content:', response.content.decode())
