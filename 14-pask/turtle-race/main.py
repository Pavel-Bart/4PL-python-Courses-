from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race. Enter a color:"
)

colors = ["red", "green", "blue", "yellow", "black"]
y_positions = [-100, -50, 0, 50, 100]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! the {winning_color} turtle is the winner")
            else:
                print(f"You lost! the {winning_color} turtle is the winner")
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

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


for i in range(0, 5):
    if winning_color == colors[i]:
        wins[i] += 1

with open("score.txt", mode="w") as file:
    scoreNum += 1
    file.write(f"{scoreName} {scoreNum}\n")
    for i in range(0, 5):
        file.write(f"{colors[i]} {wins[i]}\n")

screen.exitonclick()
