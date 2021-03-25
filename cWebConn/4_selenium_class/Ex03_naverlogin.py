"""
네이버 로그인 페이지를 실행하기
    크롬에서 네이버 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""

from selenium import webdriver

# 0. 네이버 로그인 정보
myID = 'sssw0101'
myPW = ''

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver')
driver.implicitly_wait(3) # 암묵적으로 자원로드될 때까지 3초 기다림

# 네이버로그인 하기 -[결론] 네이버 보안에 걸림
# 보안에 안걸렸으면 로그인된 상태로 많은 정보를 가져올 수 있다
driver.get('https://nid.naver.com/nidlogin.login')
# driver.find_element_by_name('id').send_keys(myID)
# driver.find_element_by_name('pw').send_keys(myPW)
# driver.execute_script("document.getElementsByName('id')[0].value=\'"+myID+"\'")
# driver.execute_script("document.getElementsByName('pw')[0].value=\'"+myPW+"\'")

# 로그인 버튼을 눌러주자.
# driver.find_element_by_id('log.login').click()

# driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Faccounts.kakao.com%2Fweblogin%2Faccount%2Finfo')

# driver.find_element_by_name('email').send_keys('sssw0101@naver.com')
# driver.find_element_by_name('password').send_keys('kim2yong1')
# driver.execute_script("document.getElementsByName('email')[0].value='sssw0101@naver.com'")
# driver.execute_script("document.getElementsByName('password')[0].value='kim2yong1'")

# driver.find_element_by_id('login-form').submit()
# driver.find_element_by_class_name('btn_confirm').click()
# driver.execute_script('document.getElementsByClassName("btn_confirm")[0].click()')

# 유튜브 로그인
driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dko%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=ko&service=youtube&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

driver.execute_script("document.getElementsByName('identifier')[0].value='sssw0101@gmail.com'")

# driver.find_element_by_name('identifier').send_keys('sssw0101@gmail.com')
# driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
# driver.find_element_by_class_name('VfPpkd-LgbsSe').click()
driver.execute_script('document.getElementsByClassName("VfPpkd-LgbsSe")[0].click()')

driver.find_element_by_name('password').send_keys('Kim2yong!')
# driver.find_element_by_xpath('//*[%id="passwordNext"]').send_keys(Keys.ENTER)


