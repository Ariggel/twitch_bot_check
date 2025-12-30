import os, requests
import os
from utils import load_config, logging_config

def get_access_token(scope : str = "public") -> str:
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
    #---- collecting all input credentials for generation of the access token ----
    client = os.environ.get('CLIENT')
    client_secret = os.environ.get('CLIENT_SECRET')
    client_user_token = os.environ.get('CLIENT_USER_TOKEN')
    redirect_uri = os.environ.get('REDIRECT_URL')

    credentials_type = {
         "public"   : "client_credentials"
        ,"private"  : "authorization_code"
    }

    required_credentials = {
         "public"   : [client, client_secret, credentials_type.get(scope,[])]
        ,"private"  : [client, client_secret, credentials_type.get(scope,[]), client_user_token, redirect_uri]
    }

    if not all(required_credentials.get(scope, [])):
        logging_config.logger_credentials.critical("client environment variables are not set")
        raise RuntimeError("missing client credentials")
    
    access_url = load_config.url_access()
    
 # ---- gather the token ----
    if scope == "public":
        params_input = {
             "client_id"        : client
            ,"client_secret"    : client_secret
            ,"grant_type"       : credentials_type.get(scope,0)
        }
        
        try:
            access_token_file = requests.post(access_url, data = params_input)
            status = access_token_file.status_code
        except Exception:
            logging_config.logger_credentials.exception("failed to retrieve access token")
            logging_config.logger_credentials.exception(f"status code: {status}")

        if status == 200:
            logging_config.logger_credentials.info("access token generation successfull")

        access_token_json = access_token_file.json()
        token = access_token_json["access_token"]

    elif scope == "private":
        params_input = {
             "client_id"        : client
            ,"client_secret"    : client_secret
            ,"code"             : client_user_token
            ,"grant_type"       : credentials_type.get(scope,0)
            ,"redirect_uri"     : redirect_uri
        }
        
        try:
            access_token_file = requests.post(access_url, data = params_input)
            status = access_token_file.status_code
        except Exception:
            logging_config.logger_credentials.exception("failed to retrieve access token")
            logging_config.logger_credentials.exception(f"status code: {status}")

        if status == 200:
            logging_config.logger_credentials.info("access token generation successfull")

        access_token_json = access_token_file.json()
        token = access_token_json["access_token"]

    return token