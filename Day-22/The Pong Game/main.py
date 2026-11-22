from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("The Pong Game")
screen.tracer(0)
scoreboard = Scoreboard()

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()

screen.listen()
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="Up", fun=r_paddle.move_up)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        # if ball is within 50 pix of the center of paddle's and far enough into x-axis then bounce
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    # R paddle
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()
    # L paddle
    elif ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()

    if scoreboard.r_score == 2:
        print("Right Wins!")
        scoreboard.game_over()
        game_on = False
    elif scoreboard.l_score == 2:
        print("Left Wins!")
        scoreboard.game_over()
        game_on = False

screen.exitonclick()