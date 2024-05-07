#!/usr/bin/python3
"""
Contains the number_of_subscribers function to retrieve subscriber count for a
subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers of the specified subreddit.
         Returns 0 if the subreddit is invalid or the request fails.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    try:
        # Make API request to get subreddit info
        url = f'http://www.reddit.com/r/{subreddit}/about.json'
        headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for invalid responses
        data = response.json()

        # Extract subscriber count from response
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    except requests.RequestException as e:
        print(f"Error occurred while fetching data: {e}")
        return 0
