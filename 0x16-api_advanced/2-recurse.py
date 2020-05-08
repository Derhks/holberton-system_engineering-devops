#!/usr/bin/python3
"""
This method return a list containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], next_pag=''):
    response = requests.get('https://www.reddit.com/r/{:s}/hot.json'.
                            format(subreddit),
                            allow_redirects=False,
                            headers={'user-agent': 'test_holberton/1.0'},
                            params={'limit': 100, 'after': '{}'.
                                    format(next_pag)})
    status = response.status_code
    list_response = response.json().get('data').get('children')
    if status == 200:
        for value in list_response:
            hot_list.append(value.get('data').get('title'))
        next_pag = response.json().get('data').get('after')
        if next_pag != 'null':
            recurse(subreddit, hot_list, next_pag)
        else:
            return hot_list
    else:
        return None


if __name__ == '__main__':
    recurse()
