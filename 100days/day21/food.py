from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        print("he is alive")
    def eat(self):

        print("no")

whale = Food()
whale.eat()