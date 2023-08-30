class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("exhale,inhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("print")


catapila = Fish()
catapila.breath()
