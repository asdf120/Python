from selenium import webdriver as driver
import cx_Oracle as oracle
import csv
from urllib import parse
import requests
import json
import folium
from bs4 import BeautifulSoup

driver = driver.Chrome('4_selenium_class/webdriver/chromedriver.exe')
driver.get('http://www.60chicken.com/bbs/board.php?bo_table=store&page=1')
html = driver.page_source  # 페이지 정보를 받아옴
soup = BeautifulSoup(html, 'html.parser')  # html 파싱
shop_name = soup.select('td.td_subject>a')

print(shop_name)