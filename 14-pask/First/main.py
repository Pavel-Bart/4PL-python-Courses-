import turtle as t
from random import randint

t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.color("green")

screen = t.Screen()


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_square(size):
    for _ in range(4):
        tim.forward(size)
        tim.left(90)


def draw_dash(dash_size, dashes):
    for _ in range(dashes):
        tim.forward(dash_size)
        tim.penup()
        tim.forward(dash_size)
        tim.pendown()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def draw_spirograph(radius, size_of_gap):
    tim.speed("fastest")
    for angle in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading() + size_of_gap)


# tim.color(random_color())
# draw_square(50)
# draw_dash(10, 10)
# draw_shape(6)
# draw_spirograph(100, 10)

def forward():
   tim.forward(50)


screen.onkeypress(forward(), "space")
screen.listen()



screen.onkeypress(tim.forward(100), "w")
screen.listen()

screen.exitonclick()

