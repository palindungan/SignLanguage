class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is {}".format(self.name))


class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False

    def introduce_self(self):
        print('Hello Nama Saya : {}'.format(self.name))


r1 = Robot('Tom', 'Red', 30)
r2 = Robot('Jerry', 'Yellow', 40)

p1 = Person('kika', 'calm', True)
p2 = Person('Zaka', 'santuy', False)

p1.robotOwned = r1

p1.robotOwned.introduce_self()
