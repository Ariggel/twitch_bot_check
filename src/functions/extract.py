import requests
import os
from utils import paths, load_config


def get_credentials() -> str:
    """
    Retrieve an App Access Token from the Twitch API using the Client Credentials flow.

    This function automates the process of obtaining a Twitch App Access Token,
    which is required to make authenticated requests to Twitch's Helix API for
    publicly accessible endpoints (e.g., user info, follows, streams).

    It reads the following environment variables:
        - CLIENT:        Your Twitch application's Client ID.
        - CLIENT_SECRET: Your Twitch application's Client Secret.

    The access token is requested from the Twitch OAuth token endpoint, using
    the 'client_credentials' grant type. The function returns the token as a
    string, which can be used in the Authorization header for subsequent API requests.

    Returns:
        str: The Twitch App Access Token.

    Notes:
        - This token typically expires after a limited time (usually 1 hour). For
          long-running scripts, it should be refreshed automatically by calling
          this function before making API requests.
        - This token only provides access to public data endpoints. Access to
          private data (e.g., subscriptions) requires a User Access Token with
          appropriate scopes.
    """
    client = os.environ.get('CLIENT')
    client_secret = os.environ.get('CLIENT_SECRET')
    access_url = load_config.url_access()

    params_input = {
         "client_id"        : client
        ,"client_secret"    : client_secret
        ,"grant_type"       : "client_credentials"
    }

    access_token_file = requests.post(access_url, data = params_input)
    access_token_json = access_token_file.json()
    return access_token_json["access_token"]


def get_user(username : str) -> dict:
    """
    Retrieve detailed information about a Twitch user by username.

    This function queries the Twitch Helix API to fetch public information
    about a specific user, such as the user ID, account creation date, 
    profile image URL, and whether a custom avatar is set.

    Parameters:
        username (str): The Twitch username of the target user.

    Returns:
        dict: A dictionary containing the following keys:
            - "id" (str): The unique Twitch user ID.
            - "date_create" (str): The ISO 8601 timestamp of when the account was created.
            - "avatar_url" (str): URL to the user's profile image.
            - "has_avatar" (bool): True if the user has a custom profile image, False if using the default.

    Notes:
        - This function internally calls get_credentials() to obtain a fresh
          App Access Token for authentication.
        - The function only returns publicly available information about the user.
    """
    api = load_config.api_users()
    client = os.environ.get('CLIENT')
    token = get_credentials()

    params_input = {
         "Client-ID"        : client
        ,"Authorization"    : f'Bearer {token}'
    }

    data_user_raw = requests.get(api, headers = params_input, params = {"login" : username})
    data_user_json = data_user_raw.json()["data"][0]
    data_user = {
         "id"           : data_user_json["id"]
        ,"date_create"  : data_user_json["created_at"]
        ,"avatar_url"   : data_user_json["profile_image_url"]
        ,"has_avatar"   : "user-default-pictures" not in data_user_json["profile_image_url"]
    }
    return data_user