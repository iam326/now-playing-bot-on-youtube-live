#!/usr/bin/env python3

import os
import urllib.parse

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']


def getYoutubeDataAPIClient():
  # Disable OAuthlib's HTTPS verification when running locally.
  # *DO NOT* leave this option enabled in production.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  api_service_name = "youtube"
  api_version = "v3"
  client_secrets_file = "client_secret.json"

  flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
      client_secrets_file, scopes)
  credentials = flow.run_console()
  return googleapiclient.discovery.build(
      api_service_name, api_version, credentials=credentials)


def getYoutubeLiveIdByUrl(url):
  qs_str = urllib.parse.urlparse(url).query
  qs = urllib.parse.parse_qs(qs_str)
  if 'v' in qs:
    return qs['v']
  return None


def main():
  url = input('Live streaming url: ')
  live_id = getYoutubeLiveIdByUrl(url)
  if live_id == None:
    print('Invalid URL')
    exit()

  youtube = getYoutubeDataAPIClient()

  live_broadcasts = youtube.liveBroadcasts().list(
      part='snippet', id=live_id).execute()

  live_chat_id = live_broadcasts['items'][0]['snippet']['liveChatId']

  youtube.liveChatMessages().insert(part='snippet', body={
      'snippet': {
          'liveChatId': live_chat_id,
          'type': 'textMessageEvent',
          'textMessageDetails': {
              'messageText': '[TEST] YouTube Live Streaming API からの送信'
          }
      }
  }).execute()


if __name__ == '__main__':
  main()
