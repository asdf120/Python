"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

"""

# 컨프리핸션 사용하지 않은 리스트 생성
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1, 7):
    alist.append(n)
print(alist)

alist = list(range(1, 7))
print(alist)
print()
# ------------------------------------------------
# 리스트 컨프리핸션
blist = [num for num in range(1, 7)]
print(blist)

blist = [n + 10 for n in range(1, 7)]
print(blist)

blist = [n for n in range(1, 7) if n % 2 == 1]
print(blist)

# [참고]
clist = [(r, c) for r in range(1, 4) for c in range(1, 3)]
print(clist)

# 컨프리헨션 없이 튜플구조의 리스트 생성
clist = []
for x in range(1, 4):
    for y in range(1, 3):
        clist.append((x, y))
print(clist)
print()
# -------------------------------------------
# 딕셔너리 컨프리핸션
datas = (2, 3, 4)
adics = {num: num ** 2 for num in datas}
print('확인 :',adics)

# 진짜 파이써닉한 코드
word = 'LOVE LOL'
wcnt = {letter: word.count(letter) for letter in word}
print(wcnt)

print()
# ------------------------------------------------
# 셋 컨프리핸션
bset = {n for n in range(1, 7)}
# print(bset)
# print(type(bset))

datas = [1, 2, 3, 2, 1, 4, 5]
bset = {n ** 2 for n in datas}
cset = set(bset)
# print(bset)
# print(cset)

# -------------------------------------------------
# [참고] 제너레이터 컨프리핸션 - 중요친않음
# ( ) 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.
# 제너레이터는 한번만 실행
# 즉석에서 그 값을 생성하고 한번에 값을 하나씩만 처리하고 저장하지 않음
datas = [1, 2, 3, 4, 5, 6, 7]
result = (n for n in datas)
print(type(result))
print(list(result))
print(list(result))
