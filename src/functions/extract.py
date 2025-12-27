import requests
from utils import paths, load_config

def get_user(username : str, streamer : str) -> any:
    api = load_config.api_users()
