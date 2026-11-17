from turtle import Screen
from snake import Snake
import time

#set up the screen
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("Snake game")
screen.listen()

#create snake object
snake = Snake()

#analyze input
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="d", fun=snake.move_right)
screen.onkey(key="w", fun=snake.move_up)
screen.onkey(key="s", fun=snake.move_down)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()