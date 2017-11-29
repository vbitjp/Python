# coding: utf-8
import re
import subprocess
from xml.etree import ElementTree 
from time import sleep
from urllib.request import Request, urlopen

# 案件カテゴリURLリストのURLごとにリクエストを投げる
# 取得したHTMLやRSSから案件のタイトルと個別案件URLのみを取得して一覧のHTMLファイルを作成する
def main():
	out_file = open("crowdworksrss.htm","w")
	cwrssList = [["クラウドワークス", ""], ["C) ハードウェア設計・開発", "crowdworks.jp/public/jobs/group/hardware_development.rss"], ["C) サイト構築", "crowdworks.jp/public/jobs/category/2/u/professionals.rss"], ["C) 業務システム", "crowdworks.jp/public/jobs/category/83/u/professionals.rss"], ["C) その他システム", "crowdworks.jp/public/jobs/category/78/u/professionals.rss"], ["C) マクロ", "crowdworks.jp/public/jobs/category/13/u/professionals.rss"], ["C) Webプログラミング", "crowdworks.jp/public/jobs/category/173/u/professionals.rss"], ["C) アプリケーション開発", "crowdworks.jp/public/jobs/category/269.rss"], ["C) アプリ・スマートフォン開発", "crowdworks.jp/public/jobs/group/software_development.rss"], ["C) ECサイト制作", "crowdworks.jp/public/jobs/category/84.rss"]]
	lancersList = [["ランサーズ", ""], ["L) ECサイト", "www.lancers.jp/work/search/web/ecdesign"], ["L) ウェブサイト制作・デザイン", "www.lancers.jp/work/search/web/website"], ["L) Webシステム開発", "www.lancers.jp/work/search/system/websystem"], ["L) 業務システム開発", "www.lancers.jp/work/search/system/software"], ["L) VBA開発", "www.lancers.jp/work/search/system/vba"], ["L) ネットワーク構築", "www.lancers.jp/work/search/system/server"], ["L) ハードウェア設計", "www.lancers.jp/work/search/system/hardware"], ["L) その他（システム開発）", "www.lancers.jp/work/search/system/othersystem"],["L) スマホアプリ・モバイル開", "www.lancers.jp/work/search/system/smartphoneapp"], ["L) アプリケーション開発", "www.lancers.jp/work/search/system/app"]]
	combiList = cwrssList + lancersList
	writeList = []
	writeList.append('<!DOCTYPE html><html lang="ja"><meta charset="UTF-8"><a name="0">TOP</a>')
	htList = FetchHtml(combiList)
	writeList = writeList + htList[0]
	writeList.append('<a name="' + str(htList[1]) + '"><a href="#0">ページTOPへ</a></a></html>')
	for line in writeList:
		out_file.write(line)
	out_file.close()
	subprocess.run(["open", "crowdworksrss.htm"], stdout=subprocess.PIPE)
	sleep(5)
	subprocess.run(["rm", "crowdworksrss.htm"], stdout=subprocess.PIPE)

# crowdworksであればRSS、lancersであればHTMLのスクレイピングを行う
def FetchHtml(urlList):
	nametagCounter = 1
	rthtmlList = []
	for work in urlList:
		# クラウドワークス用にRSSスクレイピング
		if "crowdworks.jp" in work[1]:
			h2tag = '<a name="' + str(nametagCounter) + '"><h2>' + work[0] + '<a href="#' + str(nametagCounter + 1) + '">↓</a></h2></a>'
			rthtmlList.append(h2tag)
			tree = ElementTree.fromstring(GenHtml(work[1]))
			for item in tree.findall('channel/item'):
			    title = item.find('title').text 
			    url = item.find('link').text 
			    html = '<a href = "' + url + '" target="_blank">' + title + '</a><br>'
			    rthtmlList.append(html)
			nametagCounter += 1
		# ランサーズ用にHTMLスクレイピング
		elif "lancers.jp" in work[1]:
			urlList = []
			titleList = []
			h2tag = '<a name="' + str(nametagCounter) + '"><h2>' + work[0] + '<a href="#' + str(nametagCounter + 1) + '">↓</a></h2></a>'
			rthtmlList.append(h2tag)
			text = GenHtml(work[1] + "?completed=0&sort=Work.started&direction=desc")
			for partial_html in re.findall(r'<a href="/work/detail/.*?p', text, re.DOTALL):
			    number = re.search(r'href="/work/detail/(.*?).p', partial_html).group(1)
			    url = 'https://www.lancers.jp/work/detail/' + number
			    urlList.append(url)			
			for partial_html in re.findall(r'_project.*?</a>', text, re.DOTALL):
			    partial_html = partial_html.replace("\n", "").replace(" ", "")
			    title = re.search(r'>(.*?)</a>', partial_html).group(1)
			    titleList.append(title)
			for (t1, u1) in zip(titleList, urlList):
			    html = '<a href = "' + u1 + '" target="_blank">' + t1 + '</a><br>'
			    rthtmlList.append(html)
			nametagCounter += 1
		else:
			h1tag = '<h1>' + work[0] + '</h1>'
			rthtmlList.append(h1tag)

		rthtmlList.append('<br>')
		sleep(1)
	return [rthtmlList, nametagCounter]

# URLリクエストを投げて日本語など全角文字列をHTMLタグ付きで取得する
def GenHtml(urlpart):
	url = "https://" + urlpart
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	f = urlopen(req)
	bytes_content = f.read()
	# 得られたバイトコード前半1023文字分をascii文字列にデコードする
	scanned_text = bytes_content[:1024].decode('ascii', errors='replace')
	match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
	if match:
	    encoding = match.group(1)
	else:
	    encoding = 'utf-8' 
	# 得られたバイトコードをエンコーディング指定して日本語など全角も含めた文字列にデコードする
	return bytes_content.decode(encoding)  

if __name__ == '__main__':
	main()