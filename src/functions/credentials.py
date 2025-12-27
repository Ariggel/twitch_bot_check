import os, requests
import os
from utils import load_config


def get_access_token() -> str:
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