import os, requests
from utils import load_config
from functions import credentials

def to_streamer(username : str, streamer : str) -> dict:
    api = load_config.api_follow()
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

def general(username : str) -> any:
    return