#!/usr/bin/env python3

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery


class YoutubeDataApiClient():
  def __init__(self, client_secrets_file, scopes):
    self.client = self.get_youtube_data_api_client(client_secrets_file, scopes)

  def get_youtube_data_api_client(self, client_secrets_file, scopes):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    api_service_name = "youtube"
    api_version = "v3"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    return googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

  def get_live_chat_id(self, live_id):
    live_broadcasts = self.client.liveBroadcasts().list(
        part='snippet', id=live_id).execute()

    return live_broadcasts['items'][0]['snippet']['liveChatId']

  def send_message_to_live_chat(self, live_chat_id, message):
    self.client.liveChatMessages().insert(part='snippet', body={
        'snippet': {
            'liveChatId': live_chat_id,
            'type': 'textMessageEvent',
            'textMessageDetails': {
                'messageText': message
            }
        }
    }).execute()
