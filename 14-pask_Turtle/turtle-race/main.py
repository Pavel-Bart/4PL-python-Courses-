import turtle as t
from turtle import Turtle, Screen
from random import randint


screen = t.Screen()
screen.setup(520, 400, 0, 0)
# screen.screensize(canvwidth=510, canvheight=510, bg="blue")

tim = t.Turtle()
tim.shape("turtle")
tim.penup()
tim.color("green")

joe = tim.clone()
joe.color("red")

tom = tim.clone()
tom.color("blue")

tick = tim.clone()
tick.color("black")

tack = tim.clone()
tack.color("yellow")

tim.setpos(-250, 0)
joe.setpos(-250, 50)
tick.setpos(-250, -50)
tom.setpos(-250, 100)
tack.setpos(-250, -100)


user_bet = screen.textinput("MB", "Make a bet:")
is_race_on = True


with open("score.txt") as file:
    score_data = file.readline().strip().split(" ")
    scoreName = score_data[0]
    scoreNum = int(score_data[1])

    data = file.readlines()
    colors = []
    wins = []
    for x in data:
        content = x.strip().split(" ")
        colors.append(content[0])
        wins.append(int(content[1]))

while is_race_on:
    for turtle in screen.turtles():
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()

            if user_bet == winner_color:
                print(f"Your turtle won!")
            else:
                print(f"Sorry! Won {winner_color} turtle")

        random_distance = randint(1, 10)
        turtle.forward(random_distance)

for i in range(0, 5):
    if winner_color == colors[i]:
        wins[i] += 1

with open("score.txt", mode="w") as file:
    scoreNum += 1
    file.write(f"{scoreName} {scoreNum}\n")
    for i in range(0, 5):
        file.write(f"{colors[i]} {wins[i]}\n")

screen.exitonclick()
