import feedparser

RSS_URL = "http://www.soumu.go.jp/news.rdf"
d = feedparser.parse(RSS_URL)
print(d.feed.description)
#'総務省 ホームページ新着情報 '2017/10/19配信
print(d.entries[0].title)
#'情報通信審議会 情報通信技術分科会 陸上無線通信委員会 900MHz帯自営用無線システム高度化作業班（第2回）' 2017/10/19配信
print(d.entries[0].link)
print(d.entries[1].title)
#'第481回入札監理小委員会（会議資料）'  2017/10/19配信
print(d.entries[1].link)