# 1.
pin = '880122-1234567'
birthday = '홍길도님 생년월일 : ' + pin[:6]
gender = '성별 : '
if pin[7] == '1' or '3':
    gender = gender + '남자'
elif pin[7] == '2' or '4':
    gender = gender + '여자'
else:
    print(gender + '잘못된 주민등록번호')
print(birthday)
print(gender)

# 2.
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 3.
a = ['독도는', '대한민국의', '아름다운', '섬입니다']
result = ''
for i in a:
    i = i + ' '
    result += i

print(result)

# 4.
a = (1, 2, 3)
a = a + (4,)
print(a)

# 5.
a = b = [1, 2, 3]
a[1] = 4
print(b)

# 6
i = 0;
while i < 6:
    print('{}'.format('*' * i))
    i += 1

# 7
kor_score = [77, 88, 76, 44, 56]
math_score = [96, 99, 100, 55, 66]
eng_score = [50, 60, 70, 80, 90]
midterm_score = [kor_score, math_score, eng_score]

for score in midterm_score:
    print('각 과목 총점 :', sum(score))
    print('각 과목 평균 :', round(sum(score) / len(score), 2))

result_sum = [kor + math + eng for kor, math, eng in zip(kor_score, math_score, eng_score)]
print('학생별 총점 :', result_sum)
result_avg = [round((kor + math + eng) / len(midterm_score), 2) for kor, math, eng in
              zip(kor_score, math_score, eng_score)]
print('학생별 평균 :', result_avg)

# sub = [s for s in midterm_score]result = list(enumerate(sub))for s,t in result:hap = sum(t)avg = sum(t) / len(t)print("{}과목 총점은{}이고, 평균은{:0.1f}입니다".format(s,hap,avg))score = [i for i in zip(*midterm_score)]result = list(enumerate(score))for i,j in result:hap = sum(j)avg = sum(j)/len(j)print("{}번째 학생의 총점은{}이고, 평균은{:0.1f}입니다".format(i,hap, avg))

# 8
life = {
    'animal': {
        'cats': ('Kim', 'Lee', 'Choi'),
        'octopi': 'octopi',
        'emus': 'emus'
    },
    'plants': {

    },
    'other': {

    }
}
