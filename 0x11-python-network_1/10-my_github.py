#!/usr/bin/python3
"""Take GitHub credentials (username and password) as arguments
and uses the GitHub API to display users id"""

if __name__ == '__main__':
    import sys
    import requests

     # GitHub API URL
    url = "https://api.github.com/user"

    # Send a GET request to the GitHub API with provided credentials
    response = requests.get(
        url, auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2]))

    # Parse the JSON response
    res_dict = response.json()

    # Display the user's ID
    print(res_dict.get('id'))
