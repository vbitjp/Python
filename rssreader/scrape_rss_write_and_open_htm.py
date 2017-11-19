# coding: utf-8
import re
import fileinput
import subprocess
from xml.etree import ElementTree 
from time import sleep
from urllib.request import Request, urlopen

def main():
	out_file = open("crowdworksrss.htm","w")
	cwrssList = [["ハードウェア設計・開発", "crowdworks.jp/public/jobs/group/hardware_development.rss"], ["Web開発・システム設計", "crowdworks.jp/public/jobs/category/241.rss"], ["アプリケーション開発", "crowdworks.jp/public/jobs/category/269.rss"], ["アプリ・スマートフォン開発", "crowdworks.jp/public/jobs/group/software_development.rss"], ["ECサイト制作", "crowdworks.jp/public/jobs/category/84.rss"]]
	writeList = []
	writeList.append('<!DOCTYPE html><html lang="ja"><meta charset="UTF-8">')
	nametagCounter = 0
	for work in cwrssList:
		url = "https://" + work[1]
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		f = urlopen(req)
		bytes_content = f.read()
		
		h2tag = '<a name="' + str(nametagCounter) + '"><h2>' + work[0] + '<a href="#' + str(nametagCounter + 1) + '">↓</a></h2></a>'
		writeList.append(h2tag)
		scanned_text = bytes_content[:1024].decode('ascii', errors='replace')
		match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
		if match:
		    encoding = match.group(1)
		else:
		    encoding = 'utf-8' 

		text = bytes_content.decode(encoding)  
		tree = ElementTree.fromstring(text)
		for item in tree.findall('channel/item'):
		    title = item.find('title').text 
		    url = item.find('link').text 
		    html = '<a href = "' + url + '" target="_blank">' + title + '</a><br>'
		    writeList.append(html)
		writeList.append('<br>')
		nametagCounter += 1
	writeList.append('<a name="' + str(nametagCounter) + '"><a href="#0">ページTOPへ</a></a></html>')
	for line in writeList:
		out_file.write(line)
	out_file.close()
	subprocess.run(["open", "crowdworksrss.htm"], stdout=subprocess.PIPE)
	sleep(5)
	subprocess.run(["rm", "crowdworksrss.htm"], stdout=subprocess.PIPE)

if __name__ == '__main__':
	main()