# 1.
mylist = ['apple', 'banana', 'grape']
result = list(enumerate(mylist))  # enumerate => 각 리스트에 순서를 명시
print(result)
# [(0, 'apple'), (1, 'banana'), (2, 'grape')]

# 2.
cat_song = "my cat has blue eyes, my cat is cute"
print({i: j for j, i in enumerate(cat_song.split())})  # i:j ==> 딕셔너리으로 만듦
# {'my': 5, 'cat': 6, 'has': 2, 'blue': 3, 'eyes,': 4, 'is': 7, 'cute': 8}

# 3.
colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors)
print(result)
# orange&pink&brown&black&white

# 4. ???
user_dict = {}
user_list = {'students', 'superuser', 'professor', 'employee'}
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)

# 6.
animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
print([ani for ani in animal if 'o' not in ani])
# ['DOG', 'Cat', 'Panda', 'Owl']

# 7.
name = "Hanbit University"
student = ['Hong', 'Gil', 'Dong']
split_name = name.split()
join_student = ''.join(student)
print(join_student[-4:] + split_name[1])
# DUniversity

# 8.
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

# for a, b in (alist, blist):
for (a, b) in zip(alist, blist):
    print(a, b)

# 9.
a = [1, 2, 3]
b = [4, 5, ]
c = [7, 8, 9]
print([[sum(k), len(k)] for k in zip(a, b, c)])
# [[12, 3], [15, 3]]

# 10.
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
list_data = [week, rainbow]
print(list_data[1][2])
# yellow

# 11.
kor_score = [30, 79, 20, 100, 80]
math_score = [43, 59, 0, 30, 90]
eng_score = [49, 72, 48, 67, 15]
midterm_score = [kor_score, math_score, eng_score]
print("score", midterm_score[2][1])
# score 72

# 12. 전혀모르겠음
alist = ["a", "b", "c"]
blist = ["1", "2", "3"]
abcd = []
for a, b in enumerate(zip(alist, blist)):
    print('a : ', a, 'b: ', b)
    # print(b[a])
    try:
        abcd.append(b[a])
    except IndexError:
        abcd.append("error")
    print(abcd)

# 13.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
nums = [i for i in range(20)]
answer = [alpha + str(num) for alpha in alphabet for num in nums if num % 2 == 0]
print(len(answer))


# 80

# ---------------------------------------------------------------------------------------

# 1. 다음 코드를 람다 함수 형태로 수정할 때, 알맞은 코드를 작성하시오.
def f(x, y):
    return x ** y


f = lambda x, y: x ** y

# 2. 다음과 같이 리스트 컴프리헨션으로 되어 있는 코드를 람다(lambda) 함수와 map() 함수를 사용하여 표현하시오.
ex = [1, 2, 3, 4, 5]
print([value ** 2 for value in ex])
f = lambda x: x ** 2
print(list(map(f, ex)))
print(list(map(lambda x: x ** 2, ex)))


# 3. 다음과 같이 코드를 작성했을 때, 예측되는 실행 결과를 쓰시오.
def transpose_list(two_dimensional_list):
    return [row for row in zip(*two_dimensional_list)]  # * -->


# print(transpose_list([1, 4, 7], [2, 5, 8], [3, 6, 9]))


# 4.
date_info = {'year': "2019", 'month': "9", 'day': "6"}
result = "{year}-{month}-{day}".format(**date_info)
print(result)


# 5. n개의 벡터의 크기가 동일한지 확인하는 함수를 한 줄의 코드로 작성하시오.
def vector_size_check(a, b, c):
    if len(a) == len(b) and len(a) == len(c):
        return True
    else:
        return False


a = (1, 2, 3)
b = (4, 5, 6)
c = (6, 7, 9)

print(vector_size_check(a, b, c))  # True

a = (1, 2, 3)
b = (4, 5, 6)
c = (6, 7)

print(vector_size_check(a, b, c))  # False
