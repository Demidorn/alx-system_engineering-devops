#!/usr/bin/pythom3
"""
recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit
"""


import requests


def recurse(subreddit, hot_list=[]), aftre="", count=0):
    """recursively return all hot post of subreddit"""
    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
    headers = {'Users-Agent': '0x16-api_advanced:project:
            \v1.0.0 (by /u/Demidorn)'
            }
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get('data')
    after = results.get('after')
    count += results.get('dist')

    for post in results.get('children'):
        hot_list.append(post.get('data').get('title'))

    if after is not None:
        return recursive(subreddit, hot_list, after, count)
    return hot_list
