import turtle
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(650, 550, 0, 0)
screen.tracer(0)
screen.bgcolor("lightblue")


player1 = Player(300)
player2 = Player(-300)
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")
screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")

changeX = 6
changeY = -6

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    ball.setx(ball.xcor()+changeX)
    ball.sety(ball.ycor()+changeY)

    if ball.ycor() > 260:
        ball.sety(260)
        changeY *= -1

    if ball.ycor() < -260:
        ball.sety(-260)
        changeY *= -1

    if ball.xcor() > 300:
        ball.go_to_start()
        changeY *= -1
        scoreboard.increase_player1()
        player1.go_to_start(300)
        player2.go_to_start(-300)

    if ball.xcor() < -300:
        ball.go_to_start()
        changeY *= -1
        scoreboard.increase_player2()
        player1.go_to_start(300)
        player2.go_to_start(-300)

    if ball.distance(player1) < 35:
        ball.setx(270)
        changeX *= -1

    if ball.distance(player2) < 35:
        ball.setx(-270)
        changeX *= -1


screen.exitonclick()
