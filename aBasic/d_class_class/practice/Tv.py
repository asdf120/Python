class TV(object):
    def __init__(self, size, year, company):
        self.size = size
        self.year = year
        self.company = company

    def describe(self):
        print(self.company + "에서 만든 " + self.year + "년형 " + self.size + "인치 TV")


class Laptop(TV):
    def describe(self):
        print(self.company + "에서 만든 " + self.year + "년형 " + self.size + "인치 노트북")


LG_TV = TV("32", "2019", "LG")
LG_TV.describe()
samsung_microwave = Laptop("15", "2018", "Samsung")
samsung_microwave.describe()
