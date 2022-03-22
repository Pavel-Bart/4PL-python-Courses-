from turtle import Screen
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600, 0, 0)
screen.tracer(0)


player = Player()
car_manager = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()


    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    if player.is_at_finish():
        player.go_to_start()
        score_board.increase_level()
        car_manager.level_up()

screen.exitonclick()
