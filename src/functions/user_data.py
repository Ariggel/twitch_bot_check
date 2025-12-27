import os, requests
from utils import load_config
from functions import credentials

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
    token = credentials.get_access_token()

    params_input = {
         "Client-ID"        : client
        ,"Authorization"    : f'Bearer {token}'
    }

    data_user_raw = requests.get(api, headers = params_input, params = {"login" : username})
    data_user_json = data_user_raw.json()["data"][0]
    data_user = {
         "id"               : data_user_json["id"]
        ,"date_create"      : data_user_json["created_at"][:10]
        ,"has_avatar"       : "user-default-pictures" not in data_user_json["profile_image_url"]
        ,"has_description"  : bool(data_user_json.get("description", "").strip())
    }

    return data_user