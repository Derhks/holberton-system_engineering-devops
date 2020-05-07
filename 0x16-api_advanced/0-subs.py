#!/usr/bin/python3
"""
This method returns the number the subscribers
"""
import requests


def number_of_subscribers(subreddit):
    response = requests.get('https://www.reddit.com/r/{:s}/about.json'.
                            format(subreddit),
                            headers={'user-agent': 'test_holberton/1.0'})
    if response:
        return response.json()['data']['subscribers']
    else:
        return 0

if __name__ == '__main__':
    number_of_subscribers()
