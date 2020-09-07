#!/usr/bin/env python3

import os
import urllib.parse

import spotipy

from youtube_data_api_client import YoutubeDataApiClient

SPOTIFY_API_CLIENT_SCOPE = 'user-read-currently-playing'
YOUTUBE_DATA_API_CLIENT_SCOPES = [
    'https://www.googleapis.com/auth/youtube.force-ssl']
YOUTUBE_DATA_CLIENT_SECRETS_FILE = "client_secret.json"


def main():
  username = os.environ['SPOTIPY_USERNAME']
  token = spotipy.util.prompt_for_user_token(
      username, scope=SPOTIFY_API_CLIENT_SCOPE)
  spotify = spotipy.Spotify(auth=token)

  track = spotify.current_user_playing_track()
  if track == None:
    print('no playing')
    exit()

  song_title = track['item']['name']
  singer_name = track['item']['artists'][0]['name']
  message = '♪ {} / {} #nowplaying'.format(song_title, singer_name)

  url = input('YouTube Live URL: ')
  live_id = urllib.parse.urlparse(url).path[1:]

  youtube = YoutubeDataApiClient(
      YOUTUBE_DATA_CLIENT_SECRETS_FILE, YOUTUBE_DATA_API_CLIENT_SCOPES)

  live_chat_id = youtube.get_live_chat_id(live_id)
  youtube.send_message_to_live_chat(live_chat_id, message)


if __name__ == '__main__':
  main()
