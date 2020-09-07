#!/usr/bin/env python3

import os

import spotipy


class SpotifyApiClient():
  def __init__(self, scope):
    username = os.environ['SPOTIPY_USERNAME']
    self.client = self.get_spotify_api_client(username, scope)

  def get_spotify_api_client(self, username, scope):
    token = spotipy.util.prompt_for_user_token(
        username, scope=scope)
    return spotipy.Spotify(auth=token)

  def get_now_playing_track(self):
    track = self.client.current_user_playing_track()
    if track == None:
      return None
    title = track['item']['name']
    singer = track['item']['artists'][0]['name']
    return {'title': title, 'singer': singer}
