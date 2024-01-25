#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    if count_dict is None:
        count_dict = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'custom_agent'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])

        if not posts:
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                print(f"{keyword}: {count}")
            return

        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for keyword in word_list:
                count_dict[keyword] = count_dict.get(keyword, 0) + title.count(keyword.lower())

        next_after = response.json().get('data', {}).get('after')
        return count_words(subreddit, word_list, after=next_after, count_dict=count_dict)
    else:
        return

if __name__ == "__main__":
    count_words = __import__('100-count').count_words
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
