import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.onkey(player.move, "Up")
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    cars.spawn()
    for car in cars.cars:
        if player.distance(car) < 25:
            game_is_on = False

    if player.finish():
        scoreboard.score += 1
        cars.restart()
        scoreboard.update_score()

screen.exitonclick()


