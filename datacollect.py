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
# or reference this: https://code.visualstudio.com/docs/python/environments
# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#macos-and-linux


############### Read in df of Artist Info ###############
song_data = pd.read_csv('songs_meta_table_clean2.csv')
song_data.head(n=5)
song_ids = song_data['song_uri']
print('There are ',len(song_ids), ' songs to collect audio features for')

############### Global Variables and Lists ###############
feature_list = []



############### Define Functions ###############
def getTrackFeatures(id):

    #call features from api
    features = sp.audio_features(id)

    # handling no features.
    if features[0] == None:
        track = [id, None, None, None, None, None, 
            None, None, None, None, None, None, None]
        return track

    else: 
        # extract features
        acousticness = features[0]['acousticness']
        danceability = features[0]['danceability']
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


        track = [id, acousticness, danceability, energy, instrumentalness, key, 
                liveness, loudness, mode, speechiness, tempo, time_signature, valence]
        return track
  

############### Get Song Features ############### 
# for each song call the getTrack Features function
# To return both meta data and track features.
for k in range(len(song_ids)):
    if k % 100 == 0:
        print('sleep 10 seconds')
        time.sleep(10)
    if k % 1000 == 0:
        print('sleep 1 minute')
        time.sleep(60)
    print(k)
    feature = getTrackFeatures(song_ids[k])
    print(feature)
    feature_list.append(feature)
#print(sp.audio_features(song_ids[:49]))
#convert to df
SongFeatures_df = pd.DataFrame(feature_list, columns = ['song_uri','acousticness', 'danceability', 'energy', 'instrumentalness', 
                                                        'key', 'liveness','loudness', 'mode','speechiness', 'tempo', 
                                                        'time_signature', 'valence'])
#combine it with the meta data from the songs df
SongFeatures_df = pd.merge(left = song_data, right = SongFeatures_df, left_on = 'song_uri', right_on = 'song_uri')
SongFeatures_df
#SongFeatures_df.to_csv('/Users/marysolomon/Desktop/KPOPThesis/audiofeatures_unclean.csv')

#when appending
SongFeatures_df.to_csv('/Users/marysolomon/Desktop/KPOPThesis/audiofeatures_unclean.csv', mode = 'a', header = False)