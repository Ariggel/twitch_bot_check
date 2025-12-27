import json

def api_users() -> any:
    with open('config.json','r') as file:
        config = json.load(file)
    return config['API_USERS']