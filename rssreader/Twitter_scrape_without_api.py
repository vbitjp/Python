# coding: utf-8

import urllib.request
import re

url_data = urllib.request.urlopen('https://twitter.com/crowdworks_job')
bytes_content = url_data.read()
# 得られたバイトコード前半1023文字分をascii文字列にデコードする
scanned_text = bytes_content[:1024].decode('ascii', errors='replace')
match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
if match:
    encoding = match.group(1)
else:
    encoding = 'utf-8' 
# 得られたバイトコードをエンコーディング指定して日本語など全角も含めた文字列にデコードする
text = bytes_content.decode(encoding)
for partial_html in re.findall(r'新着案件：.*?<s>', text, re.DOTALL):
    try:
        partial_html = partial_html.replace("\n", "")
        theme = re.sub(r'<(.+)>', '', partial_html)
        theme = re.sub(r'&#(.+);', '', theme)
        theme = re.sub(r'\.\.\.(.+)#crowdworks', '', theme)
        theme = re.sub(r'\.\.\.(.+)ス」', '', theme).replace("新着案件：", "")
        url = re.search(r'title="http://crowdworks\.jp/public/jobs/(.*?)"', partial_html).group(1)
        url = "http://crowdworks.jp/public/jobs/" + url
        print(theme + "| " + url)
    except AttributeError:
        print("エラー")
#print("\n" + text)