import os, requests
from utils import load_config
from functions import credentials
from utils import logging_config, exceptions

def get(username : str) -> dict:
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
    
    #---- collecting all input credentials for requesting information from Twitch API ----
    api = load_config.api_users()
    client = os.environ.get('CLIENT')
    
    if not client:
        logging_config.logger_user_data.critical("client enviroment variable is not set")
        raise RuntimeError("missing client ID")
    
    try:
        token = credentials.get_access_token()
    except Exception:
        logging_config.logger_user_data.exception("failed to retrieve access token")
        raise

    params_input = {
         "Client-ID"        : client
        ,"Authorization"    : f'Bearer {token}'
    }

    #---- sending request with all input to Twitch API ----
    try:
        data_user_raw = requests.get(api, headers = params_input, params = {"login" : username},timeout=5)
    except requests.RequestException:
        logging_config.logger_user_data.exception("network error while calling api")
        raise exceptions.TwitchAPIError("network error")
    
    #---- HTTP status handling ----
    if data_user_raw.status_code != 200:
        logging_config.logger_user_data.warning(
             "API returned error %s for user %s"
            ,data_user_raw.status_code
            ,username
        )

        if data_user_raw.status_code == 401:
            logging_config.logger_user_data.error("unauthorized")
            raise exceptions.TwitchAuthError("unauthorized")
        elif data_user_raw.status_code == 429:
            logging_config.logger_user_data.warning("request limit exceeded")
            raise exceptions.TwitchRateLimitError("request limit exceeded")
        elif data_user_raw.status_code == 400:
            logging_config.logger_user_data.critical("given parameters don't match the request query parameters")
            raise exceptions.TwitchAPIError("given parameters don't match the request query parameters")
        else:
            logging_config.logger_user_data.critical(f"unexpected return: {data_user_raw.status_code}")
            raise exceptions.TwitchBadResponse(f"unexpected return: {data_user_raw.status_code}")
    else:
        logging_config.logger_user_data.info("API request successfull for user %s", username)

    #---- selecting all necessary data from the API response ----
    try:
        data_user_json = data_user_raw.json()["data"][0]
    except ValueError:
        logging_config.logger_user_data.exception("invalid json response from API")
        raise exceptions.TwitchBadResponse("invalid json")

    data_user = {
         "id"               : data_user_json["id"]
        ,"name"             : data_user_json["display_name"]
        ,"date_create"      : data_user_json["created_at"][:10]
        ,"has_avatar"       : "user-default-pictures" not in data_user_json["profile_image_url"]
        ,"has_description"  : bool(data_user_json.get("description", "").strip())
    }

    return data_user