#!/usr/bin/env python3

import urllib.parse

from spotify_api_client import SpotifyApiClient
from youtube_data_api_client import YoutubeDataApiClient

SPOTIFY_API_CLIENT_SCOPE = 'user-read-currently-playing'
YOUTUBE_DATA_API_CLIENT_SCOPES = [
    'https://www.googleapis.com/auth/youtube.force-ssl']
YOUTUBE_DATA_CLIENT_SECRETS_FILE = "client_secret.json"


def main():
  spotify = SpotifyApiClient(SPOTIFY_API_CLIENT_SCOPE)
  youtube = YoutubeDataApiClient(
      YOUTUBE_DATA_CLIENT_SECRETS_FILE, YOUTUBE_DATA_API_CLIENT_SCOPES)

  track = spotify.get_now_playing_track()
  if track == None:
    print('no playing')
    exit()
  message = '♪ {} / {} #nowplaying'.format(track['title'], track['singer'])

  url = input('YouTube Live URL: ')
  live_id = urllib.parse.urlparse(url).path[1:]
  live_chat_id = youtube.get_live_chat_id(live_id)
  youtube.send_message_to_live_chat(live_chat_id, message)
  print(message)


if __name__ == '__main__':
  main()
