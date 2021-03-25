"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1: 'one', 2: 'two', '3': 'three', 1: '하나', 3: '셋'}
# print(dt.keys())
# print(dt.values())
# print(dt.items())
print(dt[1])
print(dt['3'])
print(dt.keys())
print()
# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1: 'one', 2: 'two', (3, 4): 'tuple'}
print(dt2[(3, 4)])

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 하나 추가할 때
dt2['korea'] = 'seoul'
print(dt2)
dt2['korea'] = 'incheon'
print(dt2)
# 여러개 추가할 때
dt2.update({'3': 'three', 4: 'four'})
print(dt2)

# [ 참고 ] 딕셔너리 생성 - dict() 이용
dt3 = dict(one='하나', two='이')
print(dt3)
print()

print('--------- 3. Key로 Value값 찾기  --------------- ')
print(dt3['one'])
print(dt3.get(1))
print(dt3.get(1,'無'))
# Key와 Value만 따로 검색
