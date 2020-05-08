#!/usr/bin/python3
"""Contains the top ten hot topics"""
import requests as re


def top_ten(subreddit):

    if subreddit is None or not isinstance(subreddit, str):
        print(None)
    headers = {'User-Agent': 'me'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    data = re.get(url, headers=headers).json()
    try:
        children = data.get('data').get('children')
        for child in children[0:10]:
            print(child.get('data').get('title'))
    except:
        print(None)
