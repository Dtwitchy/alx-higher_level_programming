#!/usr/bin/python3
"""Listing 10 commits in a repo"""

if __name__ == '__main__':
    import sys
    import requests

      # GitHub API URL to fetch commits
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2], sys.argv[1])

    try:
        # Send a GET request to the GitHub API
        response = requests.get(url)

        # Parse the JSON response
        res_dict = response.json()

        # Display the latest 10 commits
        for i in range(0, min(10, len(res_dict))):
            print("{}: {}".format(res_dict[i].get('sha'), res_dict[i].get('commit').get('author').get('name')))

    except Exception:
        pass
