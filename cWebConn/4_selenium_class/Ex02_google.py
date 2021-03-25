'''
1. 크롬웹드라이버로 구글 사이트 열기

2. 실제 크롬창에서 '플레이데이터'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='플레이데이터'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''
from selenium import webdriver
# [1]
path = './webdriver/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.implicitly_wait(2)

#----------------------------------------------
# [2]
driver.get('https://www.google.com/')

q = driver.find_element_by_name('q')
form = driver.find_element_by_id('tsf')
q.send_keys("코로나 극복")   # 검색창에 입력할 단어
form.submit()