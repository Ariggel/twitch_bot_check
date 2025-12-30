import os, requests, numpy, pandas
from functions.fnc_data import user_data
from utils import load_config
from functions import credentials

def to_streamer(username : str, streamer : str) -> dict:
     api = load_config.api_follow()
     client = os.environ.get('CLIENT')
     token = os.environ.get('CLIENT_USER_TOKEN') #credentials.get_access_token(scope = "private")     
     headers_input = {
          "Client-ID"        : client
         ,"Authorization"    : f'Bearer {token}'
     }    
     streamer_id = user_data.get(streamer)["id"]
     user_id = user_data.get(username)["id"] 
     params_input = {
          "broadcaster_id"   : streamer_id
         ,"user_id"          : user_id
     }    
     data_follow_raw = requests.get(api, headers = headers_input, params = params_input)
     data_follow_json = data_follow_raw.json().get("data",[])

     if not data_follow_json:
         data_follow = numpy.nan
         return data_follow 
     else:
          data_follow = {
                "id"               : user_id
               ,"date_follow"      : data_follow_json[0]["followed_at"][:10]
          }   
     
     dataframe = pandas.DataFrame(data_follow)

     return dataframe

