import spotipy # Spotify api
from spotipy import SpotifyOAuth
from spotipy.cache_handler import CacheHandler
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOauthError
import os # Fetches enviroment variables
import requests
import spotipy.util as util


client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')
scope='user-library-read'

def spotify_auth():
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    results = sp.current_user_saved_tracks()



    # token = util.prompt_for_user_token(scope,
    #                                 client_id,
    #                                 client_secret,
    #                                 redirect_uri="http://127.0.0.1:8000/")
    # if token: 
    #     sp = spotipy.Spotify(auth=token)
    #     results = sp.current_user_saved_tracks()
    #     for idx, item in enumerate(results['items']):
    #         track = item['track']
    #         print(idx, track['artists'][0]['name'], " – ", track['name'])
    # else:
    #     print("Can't get token for", username)