from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import *

driver = webdriver.Chrome('./webdriver/chromedriver')
driver.get('https://movie.daum.net/moviedb/grade?movieId=145835')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
score = soup.select('.ratings')
print(score)


