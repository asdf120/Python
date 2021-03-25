'''
    sum 함수 정의
        - 2개의 인자를 받아서 더한 값을 리턴
        - 그러나 다른 자료형이면
            "자료형이 달라서 계산 할 수 없다"라고 출력
            같은 자료형인 경우에만 리턴값 리턴
'''


def sum(x, y):
    if type(x) == type(y):
        return x + y
    else:
        return "자료형이 달라서 계산 할 수 없음"



# ------------------------
# 파이썬함수 역할
if __name__ == '__main__':  # 프로그램 시작점
    print(sum(2, 3))
    print(sum('hello', 'jack'))
    print(sum('hi', 100))
else:
    print('두유워너 빌더 스노맨')