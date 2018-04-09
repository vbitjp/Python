#!/usr/bin/env python3
#coding: utf-8

from requests_oauthlib import OAuth1Session
import json
import os

# 認証(環境変数からAPIキー・シークレット呼び出し)
consumer_key = os.environ['tw_consumer_key01']
consumer_secret = os.environ['tw_consumer_secret01']
access_token = os.environ['tw_access_token01']
access_token_secret = os.environ['tw_access_token_secret01']
twitter = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

# OAuth認証 セッションを開始
twitter = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

# ツイート
params = {'status': '投稿テスト with Python3'}
res = twitter.post(url_text, params = params)

# レスポンスを確認
if res.status_code == 200:
	print ("OK")
else:
    print ("テキストアップデート失敗: %s", res.text)
    exit()