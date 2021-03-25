class SoccerPlayer(object):
    def __init__(self,name,position,back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self,back_number):
        self.back_number = back_number

jinhyun = SoccerPlayer("jinhyun","MF",10)
print("현재 선수의 등번호는 :",jinhyun.back_number)
jinhyun.change_back_number(5)
print("현재 선수의 등번호는 :",jinhyun.back_number)
