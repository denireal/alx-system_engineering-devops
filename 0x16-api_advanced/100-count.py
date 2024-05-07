#!/usr/bin/python3
"""
Script to count occurrences of specific words in titles of hot posts from a subreddit.
"""

import requests

def count_words(subreddit, word_list, after='', word_dict={}):
    """
    Count occurrences of specific words in titles of hot posts from a subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.
    word_list (list): List of words to count occurrences of.
    after (str): Token for pagination (default empty string).
    word_dict (dict): Dictionary to store word counts (default empty dictionary).

    Returns:
    None
    """
    # Initialize word_dict if not provided
    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    # Base case: If after is None, print word counts sorted by frequency and alphabetically
    if after is None:
        sorted_word_dict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_dict:
            if count > 0:
                print(f'{word}: {count}')
        return None

    # Construct the URL for fetching hot posts from the subreddit
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    # Set headers and parameters for the request
    headers = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}

    # Send GET request to the Reddit API endpoint
    response = requests.get(url, headers=headers, params=parameters, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        return None

    try:
        # Extract hot posts and 'after' token from the JSON response
        hot_posts = response.json()['data']['children']
        next_after = response.json()['data']['after']

        # Process each post title to count occurrences of words in word_dict
        for post in hot_posts:
            title = post['data']['title']
            words_in_title = [word.lower() for word in title.split()]

            for word in word_dict.keys():
                word_dict[word] += words_in_title.count(word)

    except Exception:
        return None

    # Recursively call count_words with updated 'after' token and word_dict
    count_words(subreddit, word_list, next_after, word_dict)
