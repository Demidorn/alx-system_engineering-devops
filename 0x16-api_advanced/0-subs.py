#!/usr/bin/python3
"""queries the Reddit API and returns
the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers of subreddit"""
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    response = requests.get(
            url,
            headers={'User-Agent': 'Custom user agent'})
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
