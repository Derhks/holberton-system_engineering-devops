#!/usr/bin/python3
"""
This method return a list containing the titles of all hot articles
"""
import requests as req


def recurse(subreddit, hot_list=[], after=""):
    headers = {'User-agent': 'test_holberton/1.0'}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    data = req.get(url, headers=headers, allow_redirects=False).json()
    try:
        list_response = data.get('data').get('children')
        for value in list_response:
            hot_list.append(value.get('data').get('title'))
    except:
        return None

    next_pag = data.get('data').get('after')
    if next_pag is None:
        return hot_list
    return recurse(subreddit, hot_list, next_pag)
