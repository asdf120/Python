# 1.
class Calculator:
    def __init__(self, list):
        self.list = list

    def sum(self):
        sum = 0
        for num in self.list:
            sum += num
        print(sum)

    def avg(self):
        sum = 0
        for num in self.list:
            sum += num
        avg = sum / len(self.list)
        print(avg)


# cal = Calculator([1, 2, 3, 4, 5])
# cal.sum()
# cal.avg()

# 2.
# kor_score = int(input('국어점수 입력 -> '))
# eng_score = int(input('영어점수 입력 -> '))
# math_score = int(input('수학점수 입력 -> '))
# sum = kor_score + eng_score + math_score
# avg = round(sum / 3, 2)
# print('총점 :', sum, "평균 :", avg)

# 3.
def product(num, list):
    result = []
    for number in list:
        result.append(num * number)

    print(result)

# product(5,[1,2,3,4])

# 4.

def matrix_add(matrix_x, matrix_y):
    # matrix_x.extend(matrix_y)
    result = []

    for i in range(len(matrix_x)):
        list = []
        for j in range(len(matrix_x[i])):
            list.append(matrix_x[i][j] + matrix_y[i][j])
        result.append(list)
        # if num % 2 == 0:
        #     print(matrix_x[num])
        # else:
        # print(matrix_x[num])
    print(result)


matrix_x = [[2, 5], [2, 1]]
matrix_y = [[2, 4], [5, 3]]


# matrix_add(matrix_x, matrix_y)


# 5.
def vector_sub(vector):
    vector.reverse()
    print('1',vector.pop())
    result = []
    first_list = []
    first_list.append(vector[0])
    for i in range(1, len(vector)):
        for j in range(len(vector[i])):
            if i == 1:
                cal_list = first_list[0][j] - vector[i][j]
                result.append(cal_list)
            else:
                cal_list = result[0] - vector[i][j]
                result.append(cal_list)
                result.pop(0)

    return result

# def vector_sub(x):
#     x.reverse()
#     firstlist = x.pop()
#     for a in range(len(x)):
#         for b in range(len(x[a])):
#             firstlist[b] -= x[a][b]
#     return firstlist

# def vector_sub(list1):
#     rlist = []
#     for i in zip(*list1):
#         result = i[0]*2
#         for j in range(0, len(i)):
#             result += (i[j]*(-1))
#         rlist.append(result)
#     return rlist

# def vector_sub(a):
#     print(a)
#     for i,j in enumerate(a):
#         if a:
#             sum = j[0]
#             sum2= j[1]
#             a=0
#         else:
#             sum-= j[0]
#             sum2-= j[1]
#         print([sum,sum2])


print(vector_sub([[1, 3], [2, 4]]))
print(vector_sub([[1, 5], [10, 4], [4, 7],[1,1]]))
