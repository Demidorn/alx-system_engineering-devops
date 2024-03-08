#!/usr/bin/python3
"""
queries the Reddit API and prints the titles
of the first 10 hot posts listed for
a given subreddit
"""


import requests


def top_ten(subreddit):
    """prints top 10 posts of a subreddit"""
    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
    response = requests.get(
            url,
            headers={'User-Agent': 'Mozilla/5.0'},
            params={'limit': 10},
            allow_redirects=False)

    if response.status_code == 200:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
        else:
            print('None')
