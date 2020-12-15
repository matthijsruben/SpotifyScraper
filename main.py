import requests
import base64
import os
import datetime
import time

# Used for both Gmail account and Spotify account
email_address = "MBDgroup3@gmail.com"
password = "LMRSgroep3"


# Uses the 'Client Credentials Flow'
def get_access_token():
    # CLIENT_ID and CLIENT_SECRET are used for acquiring the Access Token from the Spotify Web API
    # both are connected to the dashboard application 'SpotifyScraper' connected to our spotify account
    # Accessible via 'https://developer.spotify.com/dashboard'
    CLIENT_ID = "35f1893419734fac9245f8b04101960c"
    CLIENT_SECRET = os.getenv("CLIENT_SECRET_SPOTIFY_API")
    base64_encoded = base64.b64encode((CLIENT_ID + ":" + CLIENT_SECRET).encode("ascii")).decode("ascii")

    # Officially, all parameters of the post request must be encoded in application/x-www-form-urlencoded
    # as defined in the OAuth 2.0 specification
    auth_response = requests.post("https://accounts.spotify.com/api/token", data={"grant_type": "client_credentials"},
                                  headers={"Authorization": "Basic " + base64_encoded})

    ACCESS_TOKEN = auth_response.json()["access_token"]
    expires_in = auth_response.json()["expires_in"]
    token_type = auth_response.json()["token_type"]  # should be just a string "Bearer"
    return ACCESS_TOKEN, expires_in, token_type


def 

# I guess we need threads to check every ~hour to refresh tokens
# BUFFER = 60  # 1 minute buffer just to be sure
# start = datetime.datetime.now()
# if datetime.datetime.now() > start+datetime.timedelta(seconds=expires_in-BUFFER):
#     ACCESS_TOKEN, expires_in, token_type = get_access_token()

# ACCESS_TOKEN expires in exactly 1 hour. Then a new ACCESS_TOKEN needs to be requested.
ACCESS_TOKEN, expires_in, token_type = get_access_token()

response = requests.get("https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V",
                        headers={"Authorization": token_type + " " + ACCESS_TOKEN})
print(response.json())




