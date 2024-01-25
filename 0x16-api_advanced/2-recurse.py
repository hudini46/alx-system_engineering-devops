#!/usr/bin/python3
"""
2-recurse
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    If no results are found, returns None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'custom_agent'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        if not posts:
            return hot_list
        else:
            titles = [post.get('data', {}).get('title') for post in posts]
            hot_list.extend(titles)
            next_after = response.json().get('data', {}).get('after')
            return recurse(subreddit, hot_list, after=next_after)
    else:
        return None

if __name__ == "__main__":
    recurse = __import__('2-recurse').recurse
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
