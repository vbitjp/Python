#!/usr/bin/env python3
#coding:utf-8

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
path_list_images = [
	"/Users/vbit/Desktop/images/1.png",
	"/Users/vbit/Desktop/images/2.jpg",
	"/Users/vbit/Desktop/images/3.jpg",
	"/Users/vbit/Desktop/images/4.jpg"
]

# OAuth認証 セッションを開始
twitter = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

media_ids = ""

# 画像の枚数分ループ
for path in path_list_images:
    files = {"media" : open(path, 'rb')}
    req_media = twitter.post(url_media, files = files)

    # レスポンスを確認
    if req_media.status_code != 200:
        print ("画像アップデート失敗: {}".format(req_media.text))
        exit()

    media_id = json.loads(req_media.text)['media_id']
    media_id_string = json.loads(req_media.text)['media_id_string']
    print ("Media ID: {} ".format(media_id))
    # メディアIDの文字列をカンマ","で結合
    if media_ids == "":
        media_ids += media_id_string
    else:
        media_ids = media_ids + "," + media_id_string

print ("media_ids: ", media_ids)
# Media ID を付加してテキストを投稿
params = {'status': "画像投稿テスト with Python3", "media_ids": [media_ids]}
res = twitter.post(url_text, params = params)

# レスポンスを確認
if res.status_code == 200:
	print ("OK")
else:
    print ("テキストアップデート失敗: %s", res.text)
    exit()