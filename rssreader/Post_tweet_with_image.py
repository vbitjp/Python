#!/usr/bin/env python3
#coding:utf-8
'''
This code is for tweet posting with images to Twitter API.
'''
import json
import os
from requests_oauthlib import OAuth1Session

# 認証(環境変数からAPIキー・シークレット呼び出し)
CONSUMER_KEY = os.environ['tw_consumer_key01']
CONSUMER_SECRET = os.environ['tw_consumer_secret01']
ACCESS_TOKEN = os.environ['tw_access_token01']
ACCESS_TOKEN_SECRET = os.environ['tw_access_token_secret01']
TWITTER = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

URL_MEDIA = "https://upload.twitter.com/1.1/media/upload.json"
URL_TEXT = "https://api.twitter.com/1.1/statuses/update.json"
PATH_LIST_IMAGES = [
    "/Users/vbit/Desktop/images/1.png",
    "/Users/vbit/Desktop/images/2.jpg",
    "/Users/vbit/Desktop/images/3.jpg",
    "/Users/vbit/Desktop/images/4.jpg"
]

# OAuth認証 セッションを開始
TWITTER = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

MEDIA_IDS = ""

# 画像の枚数分ループ
for path in PATH_LIST_IMAGES:
    files = {"media" : open(path, 'rb')}
    req_media = TWITTER.post(URL_MEDIA, files=files)

    # レスポンスを確認
    if req_media.status_code != 200:
        print("画像アップデート失敗: {}".format(req_media.text))
        exit()

    media_id = json.loads(req_media.text)['media_id']
    media_id_string = json.loads(req_media.text)['media_id_string']
    print("Media ID: {} ".format(media_id))
    # メディアIDの文字列をカンマ","で結合
    if MEDIA_IDS == "":
        MEDIA_IDS += media_id_string
    else:
        MEDIA_IDS = MEDIA_IDS + "," + media_id_string

print("media_ids: ", MEDIA_IDS)
# Media ID を付加してテキストを投稿
PARAMS = {'status': "画像投稿テスト with Python3", "media_ids": [MEDIA_IDS]}
RES = TWITTER .post(URL_TEXT, params=PARAMS)

# レスポンスを確認
if RES.status_code == 200:
    print("OK")
else:
    print("テキストアップデート失敗: %s", RES.text)
    exit()
