#!/usr/bin/python3
"""
This script defines a function to fetch and print the titles of the top 10
posts from a specified subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Retrieve and print the titles of the top 10 posts from a subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.

    Returns:
    None
    """
    # Construct the URL for fetching top posts from the subreddit
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set headers with a custom User-Agent to comply with Reddit API rules
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }

    # Define parameters to limit the number of posts to 10
    params = {
        "limit": 10
    }

    # Send GET request to the Reddit API endpoint
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the response status code indicates a subreddit not found (404)
    if response.status_code == 404:
        print("Subreddit not found or unavailable.")
        return

    # Extract the JSON data from the response
    results = response.json().get("data")

    # Iterate over the top 10 posts and print their titles
    [print(child.get("data").get("title")) for child in results.get("children")]
