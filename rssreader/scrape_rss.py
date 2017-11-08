import re
import sys
from xml.etree import ElementTree 
from urllib.request import Request, urlopen

req = Request('https://crowdworks.jp/public/jobs/group/software_development.rss', headers={'User-Agent': 'Mozilla/5.0'})

f = urlopen(req)
bytes_content = f.read()  

scanned_text = bytes_content[:1024].decode('ascii', errors='replace')
match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
if match:
    encoding = match.group(1)
else:
    encoding = 'utf-8' 

print('encoding:', encoding, file=sys.stderr)
text = bytes_content.decode(encoding)  
tree = ElementTree.fromstring(text)

for item in tree.findall('channel/item'):
    title = item.find('title').text 
    url = item.find('link').text 
    print(url, title)
