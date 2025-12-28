import os, requests, pandas
from utils import paths
from functions import credentials, user_data

def extract(username : str) -> dict:
    user_dict = user_data.get(username)
    return user_dict


def extract_all(username_list : list) -> pandas.DataFrame:
    data_list = []
    
    for username in username_list:
        user_extraction = extract(username)
        data_list.append(user_extraction)
    data_dataframe = pandas.DataFrame(data_list)
    return data_dataframe