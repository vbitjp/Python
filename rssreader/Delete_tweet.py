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

url_text = "https://api.twitter.com/1.1/statuses/destroy/:id.json"

# OAuth認証 セッションを開始
twitter = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

# ツイート削除(ツイートURLのhttps://twitter.com/(userid)/status/(number)のnumberに.jsonを付加してリクエスト)
res = twitter.post("https://api.twitter.com/1.1/statuses/destroy/983242687376572416.json")

# レスポンスを確認
if res.status_code == 200:
	print ("OK")
else:
    print ("テキストアップデート失敗: %s", res.text)
    exit()