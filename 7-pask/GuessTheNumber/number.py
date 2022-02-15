from random import randint
from mode import ModeItem


class Number:

    def __init__(self):
        self.number = randint(0, 100)

    def start_game(self, level: ModeItem):

        self.number = randint(0, 10)
        game_on = True
        lives = level.lives

        while game_on:

            guess = int(input("Guess the number: "))

            if guess == self.number:
                print("Congratulations!")
                game_on = False
            elif guess != self.number:
                lives -= 1

            if lives == 0:
                print(f"Sorry, you lost! Tne number was {self.number}\n")
                game_on = False
            elif game_on:
                self.help(guess)

    def help(self, guess):
        if guess < self.number:
            print(f"Answer is greater than {guess}. Try again!")
        else:
            print(f"Answer is smaller than {guess}. Try again")
