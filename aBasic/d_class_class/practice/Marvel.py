class Marvel(object):
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic

    def __str__(self):
        return "My name is {}, and my weapon is {}.".format(self.name, self.characteristic)


class Villian(Marvel):
    pass


first_villain = Villian("Thanos", "infinity gauntlet")
print(first_villain)
