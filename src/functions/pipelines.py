import os, requests
from utils import paths
from functions import credentials, user_data

def extract(username) -> dict:
    user_dict = user_data.get_user(username)
    return user_dict
    