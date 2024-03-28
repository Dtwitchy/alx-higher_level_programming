#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header"""

if __name__ == '__main__':
    import sys
    import requests
    try:
         url = sys.argv[1]
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
    except Exception:
        pass
