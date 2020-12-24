## Import libraries :D
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import os
from itertools import chain

## Authenticate the Spoitify api using spotipy
client_id = 'feeecba2878a47008aa8359b6a24b4c2'
client_secret = '5c08310205a943d8a995cba8fdb83c78'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#later figure out how to set up api with global config file so that keys are anonymous.


## Define Artist URIs



## Define Functions

print(sp.artist_albums(artist_id = 'spotify:artist:52Gsa9Zypqztm2DeNkQfCm', limit = 50))
