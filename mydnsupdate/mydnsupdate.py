# coding: utf-8

from __future__ import division
import ui
import clipboard
from console import hud_alert
import urllib.parse
import urllib.request
from datetime import datetime
import sys

def mydnsupdate():
	url = "https://ipv4.mydns.jp/login.html"
	request = urllib.request.Request(url)
	request.add_header('Content-Type', 'application/json; charset=utf-8')
	request.add_header('Authorization', 'Basic bXlkbnMwMDAwMDA6MDEyMzQ1Njc4OWFi')
#Login ID=mydns000000, Password=0123456789ab の場合、IDとパスワードをコロン:でつないで、
#mydns000000:0123456789ab をBase64エンコードするとbXlkbnMwMDAwMDA6MDEyMzQ1Njc4OWFi になる
	request.get_method = lambda: "GET"
	
	f = urllib.request.urlopen(request)
	global response
	response = f.read()
	
def button_tapped(sender):
	'@type sender: ui.Button'
	# Get the button's title for the following logic:
	t = sender.title
	# Get the labels:
	label = sender.superview['label1']
	if t == 'Update':
		mydnsupdate()
		label.text = str(response)
		
v = ui.load_view('mydnsupdateui')

if min(ui.get_screen_size()) >= 768:
	# iPad
	v.frame = (0, 0, 360, 400)
	v.present('sheet')
else:
	# iPhone
	v.present(orientations=['portrait'])
