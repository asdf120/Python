# -----------------------------------------------
#  집합
#       - 집합에 관련된 자료형
#       - 순서를 지정하지 않는다
#       - 중복을 허용하지 않는다


# s = set()               # 빈 집합을 생성
s = set([1,2,3,1,1])
a = set([3,'dog',7,5,1,'abc'])
print(s)
print(a)
s3 = {3,4,5,6}
print(s3)

print(s.intersection(s3))   # 교집합
print(s.union(s3))  # 합집합
print(s - s3)   # 차집합
print()
print(s & s3)
print(s | s3)
print()

#-------------------------
# [ 참고 ]
# 숫자인 경우에 0 - False, 0이 아닌경우 True
a = 10
b = -1
if a and b:
    print("True1")
if a or b:
    print("True2")
print(a and b)
print(a or b)

print(s and s3)
print(s or s3)