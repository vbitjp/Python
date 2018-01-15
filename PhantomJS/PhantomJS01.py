# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# PhantomJSのWebDriverを作成する。 
driver = webdriver.PhantomJS()
# Googleのトップ画面を開く。 
driver.get('http://www.google.co.jp')
# タイトルに'Google'が含まれていることを確認する。 
assert 'Google' in driver.title
# 検索語を入力して送信する。
input_element = driver.find_element_by_name('q') 
input_element.send_keys('Python') 
input_element.send_keys(Keys.RETURN)
# タイトルに'Python'が含まれていることを確認する。 
assert 'Python' in driver.title
# スクリーンショットを撮る。 
driver.save_screenshot('search_results.png')
for a in driver.find_elements_by_css_selector('h3 > a'):
    print(a.text)
    print(a.get_attribute('href'))