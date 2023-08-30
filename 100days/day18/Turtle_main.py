from turtle import Turtle, Screen

tim = Turtle()


def mover():
    tim.forward(200)


def back():
    tim.backward(30)
def clear():
    tim.clearstamps(30)
def back():
    tim.backward(30)


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=mover)
screen.onkey(key="s", fun=back)
# screen.onkey(key="a", fun=c_clock)
# screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
