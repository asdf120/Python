"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""


class Sample:
    data = 'hello'  # 멤버변수 선언 (지양)

    # 생성자역할  # 클래스변수가 생성됨과 동시에 호출
    def __init__(self):
        self.age = 25  # 멤버변수 선언
        self.name = '홍길동'
        print('__init__')

    # 소멸자역할
    def __del__(self):
        print('__del__')


sample = Sample()
print(sample.data, sample.name)
print(str(sample.age) + '세')
del sample  # 메모리 종료시점을 지정가능
print('프로그램 종료')

"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
    
    [참고] static 함수 --> 사장됨
 
"""


class Book:
    cnt = 0

    def __init__(self, title):
        # TODO 매개변수(지역)을 멤버변수 지정
        self.title = title

    # 인스턴스 함수 : 클래스 안에 일반 함수
    def output(self):
        print('제목 output:', self.title)
        self.cnt += 1
        print('갯수:', self.cnt)

    # 클래스 함수
    @classmethod
    def output2(cls):
        # print('제목',cls.title)
        cls.cnt += 1
        print('갯수:', cls.cnt)


book = Book('정의란')
book2 = Book('다이어트란')

book.output()
book2.output()
print('-' * 50)
book.output2()
book2.output2()
Book.output2()

'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''


class Animal:
    def move(self):
        print('동물은 움직인다')


class Wolf(Animal):  # 늑대는 동물을 상속
    def move(self):
        print('늑대는 뛴다')


class Human(Animal):
    def move(self):
        print('사람은 두발로 걷는다')


class Wear_wolf(Wolf, Human):
    def move(self):
        print('늑대인간은 두발로 달린다')
        super().move()


wearWolf = Wear_wolf()
wearWolf.move()
