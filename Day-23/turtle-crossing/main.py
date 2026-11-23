import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.tracer(0)
screen.listen()

user = Player()
level = Scoreboard()
screen.onkey(key="w", fun=user.move)

car_list = []
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # 1 in 6 chance a car is created
    if random.randint(1, 6) == 1:
        cars = CarManager()
        car_list.append(cars)

    for car in car_list:
        car.move(level.level)

        if user.distance(car) < 20:
            level.game_over()
            game_is_on = False

        elif user.ycor() > 280:
            level.score()
            user.restart()

screen.exitonclick()