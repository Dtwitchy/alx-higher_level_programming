#!/usr/bin/python3
"""A Python script that takes a URL and an email,
sends a POST request to the provided URL with the email as a parameter,
and displays the body of the response (decoded in UTF-8)."""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    target_url = sys.argv[1]
    email_data = {'email': sys.argv[2]}
    encoded_email = urllib.parse.urlencode(email_data)
    encoded_email = encoded_email.encode('ascii')
    request = urllib.request.Request(target_url, encoded_email)

    with urllib.request.urlopen(request) as response:
        url_resp = response.read()
    
    decoded_output = url_resp.decode('utf-8')
    print(decoded_output)
