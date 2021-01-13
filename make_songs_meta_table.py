############### Import libraries :D ###############
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
import time
import os
from itertools import chain


############### Authenticate the Spoitify api using spotipy ###############
client_id = 'feeecba2878a47008aa8359b6a24b4c2'
client_secret = '5c08310205a943d8a995cba8fdb83c78'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

############### Read in df of Artist Info ###############
artist_data = pd.read_csv('artist_df.csv').tail(1)
artist_data.head(n=5)
artist_list = artist_data['ID']

############### Global Variables and Lists ###############
song_ids = []
meta_list = []


############### Define Functions ###############
def getMetaFeatures(id):
  meta = sp.track(id)

  # meta
  name = meta['name']
  uri = meta['uri']
  album = meta['album']['name']
  album_uri = meta['album']['uri']
  artist = meta['album']['artists'][0]['name']
  artist_uri = meta['album']['artists'][0]['uri']
  release_date = meta['album']['release_date']
  popularity = meta['popularity']
  available_markets = meta['available_markets']
  duration_ms = meta['duration_ms']


  track_meta = [name, uri, album, album_uri, artist, artist_uri, release_date, popularity, duration_ms]
  return track_meta


############### Get Song IDs for each artist ###############
for artist in artist_list:
    ## Limit value must be between 1 and 50
    artistalbums = sp.artist_albums(artist_id = artist, limit = 50)
    
    
    # go to their individual albums
    for i in range(len(artistalbums['items'])):
        album_uri = artistalbums['items'][i]['uri']
        album_tracks = sp.album_tracks(album_uri)
        
        #go to their individual tracks
        for j in range(len(album_tracks['items'])):
            song_ids.append(album_tracks['items'][j]['uri'])
            #song_ids.append(album_tracks['items'][j]['id'])

#print(song_ids)
print(type(song_ids))
print(len(song_ids))
#remove duplicates
song_ids = list(set(song_ids))
print(type(song_ids))
print(len(song_ids))

for k in range(len(song_ids)):
    meta = getMetaFeatures(song_ids[k])
    if k % 100 == 0:
        print('sleep 10 seconds')
        time.sleep(10)
    if k % 1000 == 0:
        print('sleep 1 minute')
        time.sleep(60)
    print(k)
    print(meta)
    meta_list.append(meta)

#convert to df
MetaFeatures_df = pd.DataFrame(meta_list, columns = ['song_name', 'song_uri', 'album', 'album_uri',  'artist', 'artist_uri',
                                     'release_date', 'popularity', 'duration_ms'])
MetaFeatures_df
MetaFeatures_df.to_csv('/Users/marysolomon/Desktop/KPOPThesis/songs_meta_table_unclean.csv')