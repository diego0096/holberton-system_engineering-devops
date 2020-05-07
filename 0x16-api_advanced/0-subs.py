#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import requests as re


def number_of_subscribers(subreddit):
"""returns the number of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {'User-Agent': 'me'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = re.get(url, headers=headers).json()
    try:
        return (data.get('data').get('subscribers'))
    except:
        return 0
