"""
    비밀번호 생성시 의 적합성 체크
    1. 비밀번호의 길이는 6-10
    2. 숫자와 알파벳으로만 구성되어야 함
    3. 대문자와 소문자가 섞여야 함 ( 대문자 1개 이상, 소문자 0개 이상)
    4. 위의 조건에 부합하면 잘못된 상황을 출력하고
       조건을 모두 만족하면 가능한 비밀번호임을 출력한다.
"""

import re


def pwd_check(pwd):
    # 여기에 코드 작성
    pattern = re.compile(r'^[a-zA-Z0-9]+')
    result = pattern.search(pwd)
    if len(pwd) >= 6 and len(pwd) <= 10:
        if result:
            print('맞는형식의 비밀번호')
        else:
            print("비밀번호를 재설정")
    else:
        print("비밀번호는 6 ~ 10자 설정")
    return


pwd_check('abcdE')  # 길이오류
pwd_check('abcdef')  # 대문자 포함하지 않아 오류
pwd_check('Abcdef2')  # 성공
pwd_check('Abcdef_2')  # 특수문자 포함
pwd_check('Abcddddddef_2')  # 특수문자 포함
