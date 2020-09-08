# now-playing-bot-on-youtube-live

YouTube Live のチャットにて、現在 Spotify で再生中の曲を定期的に呟く BOT

## 前提条件

* GCP アカウントが作成済みであること
* Spotify Premium に登録済みであること

## 環境

```
$ sw_vers
ProductName:	Mac OS X
ProductVersion:	10.14.6
BuildVersion:	18G103

$ python --version
Python 3.7.5

$ pip --version
pip 19.2.3 from /Users/<USERNAME>/Library/Python/3.7/lib/python/site-packages/pip (python 3.7)
```

## Setup

```
$ pip install -r requirements.txt

$ export SPOTIPY_USERNAME="<USER_NAME>"
$ export SPOTIPY_CLIENT_ID="<CLIENT_ID>"
$ export SPOTIPY_CLIENT_SECRET="<CLIENT_SECRET>"
$ export SPOTIPY_REDIRECT_URI="<REDIRECT_URL>"
```

## Usage

```
$ python main.py
...
```
