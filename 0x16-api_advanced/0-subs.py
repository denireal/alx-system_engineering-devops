#!/usr/bin/python3
"""
Contains the number_of_subscribers function to retrieve subscriber count for a
subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    # Set a custom User-Agent header to avoid Reddit API rate limiting
    headers = {"User-Agent": "MyAPI/1.0.0"}

    # Construct the URL for the subreddit's about.json API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Send a GET request to the Reddit API endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response and retrieve the subscriber count
        data = response.json().get("data", None)
        if data:
            subscribers = data.get("subscribers", 0)
            return subscribers
        else:
            # Invalid subreddit may return empty data, handle as not found
            return 0
    else:
        # If request fails or subreddit is not found (404), return 0
        return 0


# Main script logic (for standalone usage)
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        num_subscribers = number_of_subscribers(subreddit_name)
        print(num_subscribers)
