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

# 情報取得
api = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
params = {'since':"2018-04-08",'count': 2} # 日付指定sinceは無くても最新ツイートから検索可
res = twitter.get(api, params = params)
if res.status_code == 200:

    timeline = json.loads(res.text)
    for tweet in timeline:
        print(tweet["user"]["name"], tweet["text"]) # ユーザ名とツイートのみ書き出し

else:
    print ("Error: %d" % res.status_code)
