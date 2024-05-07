#!/usr/bin/python3
"""
This script defines a recursive function to recursively fetch all titles from the hot posts
of a specified subreddit using Reddit's API.
"""

import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieve all titles from the hot posts of a subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.
    hot_list (list): List to store titles of hot posts (default empty list).
    after (str): A token used for pagination (default empty string).
    count (int): Total count of posts fetched (default 0).

    Returns:
    list: A list containing titles of all hot posts from the specified subreddit.
          Returns None if the subreddit is not found or the request fails.
    """
    # Construct the URL for fetching hot posts from the subreddit
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set headers with a custom User-Agent to comply with Reddit API rules
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }

    # Define parameters including 'after' token for pagination and 'limit' for number of posts
    params = {
        "after": after,
        "count": count,
        "limit": 100  # Fetch up to 100 posts per request
    }

    # Send GET request to the Reddit API endpoint
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the response status code indicates a subreddit not found (404)
    if response.status_code == 404:
        return None

    # Extract the JSON data from the response
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # Iterate over the posts and append their titles to the hot_list
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    # Recursively call the function if 'after' token is not None (more posts available)
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Return the accumulated list of titles
    return hot_list
