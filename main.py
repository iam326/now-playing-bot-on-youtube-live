#!/usr/bin/env python3

import os
import spotipy


def main():
  username = os.environ['SPOTIPY_USERNAME']
  scope = 'user-read-currently-playing'
  token = spotipy.util.prompt_for_user_token(username, scope=scope)
  spotify = spotipy.Spotify(auth=token)

  track = spotify.current_user_playing_track()
  if track == None:
    print('no playing')
    exit()

  song_title = track['item']['name']
  singer_name = track['item']['artists'][0]['name']
  print('♪ {} / {} #nowplaying'.format(song_title, singer_name))


if __name__ == '__main__':
  main()
