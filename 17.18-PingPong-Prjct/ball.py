from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.go_to_start()
        self.speed(0)

    def go_to_start(self):
        self.goto(0, 0)
