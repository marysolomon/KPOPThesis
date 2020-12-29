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
#later figure out how to set up api with global config file so that keys are anonymous.
#reference this:  https://towardsdatascience.com/how-to-hide-your-api-keys-in-python-fb2e1a61b0a0


############### Read in df of Artist Info ###############
artist_data = pd.read_csv('artist_df.csv')
#print(artist_data)
artist_list = artist_data['ID']
print(artist_list[:5])
print(type(artist_list))


############### Global Variables and Lists ###############
song_ids = []
feature_list = []



############### Define Functions ###############

def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

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

  # audio features not available if song is unavailable in any market
  # prevent error :line 51, in getTrackFeatures
  # acousticness = features[0]['acousticness']
  # TypeError: 'NoneType' object is not subscriptable
  if len(available_markets) == 0:
      track = [uri, name, album, album_uri, artist, artist_uri, release_date, popularity, None, None, None,
             None, None, None, None, None, None, None, None, None, None]
      return track

  # As long as song is available in any market, get all of the audio features :D
  else: 
    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    duration_ms = meta['duration_ms']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    key = features[0]['key']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    mode = features[0]['mode']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']
    valence = features[0]['valence']

    track = [uri, name, album, album_uri, artist, artist_uri, release_date, popularity, acousticness, danceability, duration_ms,
             energy, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time_signature, valence]
    return track
  



# def getMetaFeatures(id):
#   meta = sp.track(id) 

#   # meta
#   name = meta['name']
#   uri = meta['uri']
#   album = meta['album']['name']
#   album_uri = meta['album']['uri']
#   artist = meta['album']['artists'][0]['name']
#   artist_uri = meta['album']['artists'][0]['uri']
#   release_date = meta['album']['release_date']
#   popularity = meta['popularity']
#   duration_ms = meta['duration_ms']

#   meta_track = [uri, name, album, album_uri, artist, artist_uri, 
#                 release_date, popularity, duration_ms]
#   return meta_track

# def getTrackFeatures(id):
#   features = sp.audio_features(id)

#   # features
#   acousticness = features[0]['acousticness']
#   danceability = features[0]['danceability']
#   energy = features[0]['energy']
#   instrumentalness = features[0]['instrumentalness']
#   key = features[0]['key']
#   liveness = features[0]['liveness']
#   loudness = features[0]['loudness']
#   mode = features[0]['mode']
#   speechiness = features[0]['speechiness']
#   tempo = features[0]['tempo']
#   time_signature = features[0]['time_signature']
#   valence = features[0]['valence']

#   track = [acousticness, danceability, energy, instrumentalness, 
#             key, liveness, loudness, mode, speechiness, tempo, time_signature, valence]
#   return track

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
song_ids = pd.DataFrame(song_ids).drop_duplicates()[0].tolist()
print(len(song_ids))

############### Create Song Metadata DF ############### 
# This contains data on song names, album names, artist names, 
# as well as the unique identifiers (URIS)


############### Clean Song list ############### 
# remove 'live', 'tour', 'the best of' albums since they are repeats of the songs that exist on albums
# remove songs that actually don't have the artists in our list as the main artist (compilation albums)
# remove instrumental versions of songs
## ?? remove the kingdom and queendom albums (from a competition show) ??
## ?? remove japanese and english versions of songs ??



############### Get Song Features ############### 
# for each song call the getTrack Features function
# To return both meta data and track features.
for k in range(len(song_ids)):
    if k % 100 == 0:
        print('sleep 10 seconds')
        time.sleep(10)
    else:
        time.sleep(0.5)
    print(k)
    feature = getTrackFeatures(song_ids[k])
    print(feature)
    feature_list.append(feature)
#print(sp.audio_features(song_ids[:49]))
#convert to df
SongFeatures_df = pd.DataFrame(feature_list, columns = ['song_name', 'song_uri', 'album', 'album_uri','artist', 'artist_uri','release_date', 'popularity', 'acousticness', 
                                     'danceability','duration_ms', 'energy', 'instrumentalness', 'key', 
                                     'liveness','loudness', 'mode','speechiness', 'tempo', 'time_signature', 'valence'])
SongFeatures_df
SongFeatures_df.to_csv('/Users/marysolomon/Desktop/KPOPThesis/songfeatures_unclean.csv')