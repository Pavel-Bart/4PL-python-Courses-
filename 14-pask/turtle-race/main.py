import turtle as t
from random import randint

screen = t.Screen()
screen.setup(500, 500, 0, 0)


tim = t.Turtle()
tim.shape("turtle")
tim.penup()
tim.color("green")

joe = tim.clone()
joe.color("red")

tom = tim.clone()
tom.color("blue")

tim.goto(-250, 0)
joe.goto(-250, 50)
tom.goto(-250, 100)

tim.speed(2)
joe.speed(1)
tim.pendown()
joe.pendown()

tim.forward(499)
joe.forward(482)


def random_speed():
    speed = randint(0, 10)
    return speed


screen.exitonclick()
