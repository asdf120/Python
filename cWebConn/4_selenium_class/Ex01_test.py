"""
 간단하게 크롬 브라우저를 실행하여 페이지 열기
"""

from selenium import webdriver

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(2)
    # selenium은 기본적으로 웹 자원들이 로드될 때까지 대기하지만
    # 암묵적으로 기다리기 위해 2초 여유를 지정

# 2. 페이지 접근
driver.get('https://www.daum.net/')

# 3. 화면을 캡처해서 저장하기
driver.save_screenshot('daum_main.png')