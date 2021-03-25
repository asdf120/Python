msg = '행복해'  # 문자열
li = ['a', 'b', 'c']  # 리스트
tpl = ('ㄱ', 'ㄴ', 'ㄷ')  # 튜플
di = {'k': 5, 'j': 6, 'l': 7}  # 딕셔너리

# unpacking : 각요소를 분해
# c1, c2, c3, c4 = msg  # 자리수 딱 맞춰야 언팩킹가능 3글자인데 c2 c4까지 설정하면 에러뜬다.
# 각 요소의 수와 변수의 수는 맞춰야 된다.
# print(c1, c2, c3, c4)
a1, a2, a3 = li
print(a1, a2, a3)

b1, b2, b3 = tpl
print(b1, b2, b3)

d1, d2, d3 = di  # 딕셔너리는 키값만 가져옴.
print(d1, d2, d3)

d1, d2, d3 = di.items()  # 이렇게하면 키값 밸류값 다 가져옴.
print(d1, d2, d3)

d1, d2, d3 = di.values()  # 이거는 밸류값만 가져옴.
print(d1, d2, d3)

# Dictionary는 반복문을 이용하여 key와 value 출력
for key, value in di.items():
    print(key, "  ", value)

alist = [(1, 2), (3, 4), (5, 6)]
for result in alist:
    print(result)
for first, second in alist:
    print('first + second = {}'.format(first + second))
print()
# ----------------------------------------------------
# [2] enumerate ()
# 각 리스트에 순서를 명시해주는 함수
user_list = ['개발자', '코더', '전문가', '분석가']
for value in user_list:
    print(value)
for idx, value in enumerate(user_list):
    print(idx, value)

# ----------------------------------------------------
# [3] TODO zip() 중요
days = ['월', '화', '수']
doit = ['잠자기', '밥먹기', '공부하기']
print(zip(days, doit))
print(list(zip(days, doit)))
print(dict(zip(days, doit)))

for (a, b) in zip(days, doit):
    print("{}요일에는 {}를 합니다".format(a, b))
