from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import os
import json

load_dotenv()

def get_mutual_followers():
    api_key = os.getenv('X_API_KEY')
    api_secret = os.getenv('X_API_SECRET')
    access_token = os.getenv('X_ACCESS_TOKEN')
    access_token_secret = os.getenv('X_ACCESS_TOKEN_SECRET')

    x = OAuth1Session(api_key, client_secret=api_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)

    # Fetch followers (users following you)
    followers_url = "https://api.x.com/2/users/me/following"
    following_response = x.get(followers_url, params={'user.fields': 'username'})
    following = following_response.json().get('data', [])

    # Find mutual followers
    follower_usernames = {f['username'] for f in followers}
    following_usernames = {f['username'] for f in following}
    mutual_followers = [{'username': username} for username in follower_usernames.intersection(following_usernames)]

    return mutual_followers