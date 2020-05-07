#!/usr/bin/python3
"""
This method prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    response = requests.get('https://www.reddit.com/r/{:s}/hot.json'.
                            format(subreddit),
                            allow_redirects=False,
                            headers={'user-agent': 'test_holberton/1.0'},
                            params={'limit': 10})
    status = response.status_code
    if status == 200:
        for cnt in range(10):
            print(response.json()['data']['children'][cnt]['data']['title'])
    else:
        print(None)


if __name__ == '__main__':
    top_ten()
