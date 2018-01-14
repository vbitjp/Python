# coding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chrome Driverの実行オプションを設定
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
chrome_driver_path = '/Users/vbit/chromedriver'

browser = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
url_str = 'https://vbit.jp'
browser.get(url_str)
html = browser.page_source
browser.close()
print(html)
