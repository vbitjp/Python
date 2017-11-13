# coding: utf-8
import re
import sys
import fileinput
import subprocess
from xml.etree import ElementTree 
from urllib.request import Request, urlopen

out_file = open("crowdworksrss.htm","w")
req = Request('https://crowdworks.jp/public/jobs/group/development.rss', headers={'User-Agent': 'Mozilla/5.0'})

f = urlopen(req)
bytes_content = f.read()  

scanned_text = bytes_content[:1024].decode('ascii', errors='replace')
match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
if match:
    encoding = match.group(1)
else:
    encoding = 'utf-8' 

#print('encoding:', encoding, file=sys.stderr)
text = bytes_content.decode(encoding)  
tree = ElementTree.fromstring(text)
out_file.write('<!DOCTYPE html><html lang="ja"><meta charset="UTF-8">')

for item in tree.findall('channel/item'):
    title = item.find('title').text 
    url = item.find('link').text 
    html = '<a href = "' + url + '" target="_blank">' + title + '</a><br>'
    out_file.write(html)
out_file.write('</html>')
out_file.close()
subprocess.run(["open", "crowdworksrss.htm"], stdout=subprocess.PIPE)
subprocess.run(["rm", "crowdworksrss.htm"], stdout=subprocess.PIPE)