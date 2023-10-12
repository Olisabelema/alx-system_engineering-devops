#!/usr/bin/python3
"""Advanced Apis Module"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None,):
    """function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit."""

    headers = {"User-Agent": "user_agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(
        subreddit)
    params = {"limit": 100, "after": after}

    response = requests.get(
        url=url,
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        children = data['children']
        hot_list.extend([child['data']['title']
                         for child in children])
        after = response.json()['data']['after']
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subred = sys.argv[1]
        recurse(subred, [])
