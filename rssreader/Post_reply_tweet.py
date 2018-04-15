#!/usr/bin/env python3
#coding:utf-8
'''
This code is for reply posting to Twitter API.
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

# OAuth認証 セッションを開始
TWITTER = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# ツイート
PARAMS = {'status': 'リプライ投稿テスト with Python3', 'in_reply_to_status_id':985515959312986112}
RES = TWITTER .post(URL_TEXT, params=PARAMS)

# レスポンスを確認
if RES.status_code == 200:
    print("OK")
else:
    print("テキストアップデート失敗: %s", RES.text)
    exit()
