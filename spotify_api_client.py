#!/usr/bin/env python3

import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyApiClient():
    def __init__(
            self,
            username,
            client_id,
            client_secret,
            redirect_uri,
            scope):

        self.__auth_manager = SpotifyOAuth(
            username=username,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope)
        self.__client = spotipy.Spotify(auth_manager=self.__auth_manager)

    def get_client(self):
        self.__auth_manager.get_access_token(as_dict=False)
        return self.__client

    def get_now_playing_track(self):
        track = self.get_client().current_user_playing_track()
        if track is None:
            return None

        title = track['item']['name']
        singer = track['item']['artists'][0]['name']

        return {
            'title': title, 'singer': singer
        }
