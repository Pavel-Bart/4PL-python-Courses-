from turtle import Turtle

MOVE_DISTANCE = 20


class Player(Turtle):

    def __init__(self, starting_x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=6)
        self.penup()
        self.setheading(90)
        self.go_to_start(starting_x)

    def go_to_start(self, starting_x):
        self.goto(starting_x, 0)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)
