from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#set up the screen
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("Snake game")
screen.listen()

#create objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    #if head collides with any segment
    for segment in snake.snake_segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()