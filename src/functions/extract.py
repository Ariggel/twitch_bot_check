import requests
import os
from utils import paths, load_config


def get_credentials() -> any:
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

def get_user(username : str, streamer : str) -> any:
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
    }
    return data_user