#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    target_url = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(target_url) as response:
            response_body = response.read()
            print(response_body.decode('utf-8'))

    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
