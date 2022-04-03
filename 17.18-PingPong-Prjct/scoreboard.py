from turtle import Turtle

FONT = ("Roboto", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f" {self.score1} : {self.score2}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over!", align="center", font=FONT)

    def increase_player1(self):
        self.score1 += 1
        self.update_scoreboard()

    def increase_player2(self):
        self.score2 += 1
        self.update_scoreboard()
