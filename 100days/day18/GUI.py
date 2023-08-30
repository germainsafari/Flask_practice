import random
from Turtle_main import Turtle, Screen


Germain_the_goat = Turtle()
Germain_the_goat.shape("turtle")

colors = ["red", "green", "blue"]

def run(num_of_sides):
    for _ in range(num_of_sides):
        angle = 360 / num_of_sides
        Germain_the_goat.forward(100)
        Germain_the_goat.right(angle)


for i in range(3, 11):
    Germain_the_goat.color(random.choice(colors))
    run(i)
# for _ in range(4):
#     Germain_the_goat.forward(100)
#     Germain_the_goat.right(90)
#     Germain_the_goat.color("red")
# for _ in range(5):
#     Germain_the_goat.forward(100)
#     Germain_the_goat.right(72)
# for _ in range(6):
#     Germain_the_goat.forward(100)
#     Germain_the_goat.right(60)
# for _ in range(7):
#     Germain_the_goat.forward(100)
#     Germain_the_goat.right(51.4)
# for _ in range(8):
#     Germain_the_goat.forward(100)
#     Germain_the_goat.right(45)
# for _ in range(9):
#     Germain_the_goat.forward(100)
#     Germain_the_goat.right(40)

screen = Screen()
screen.exitonclick()