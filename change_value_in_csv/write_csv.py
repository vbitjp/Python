#!/usr/local/bin/python3.4
# coding: utf-8
import csv
#import codecs

with open('top_cities.csv', 'w', newline='') as f:
#with codecs.open('top_cities.csv', 'w', 'utf-8') as f:
#ロリポップのレンサバで書き出す場合、文字コードの環境がJISなのか不明だが
#codecsモジュールでutf-8を呼び出さないとutf-8として日本語を書き込めないので注意
    a = '上海'
    b = 'カラチ'
    c = '北京'
    d = '天津'
    e = 'イスタンブル'
    writer = csv.writer(f) 
    writer.writerow(['rank', 'city', 'population'])  
    writer.writerows([
        [1, a, 24150000],
        [2, b, 23500000],
        [3, c, 21516000],
        [4, d, 14722100],
        [5, e, 14160467],
    ])