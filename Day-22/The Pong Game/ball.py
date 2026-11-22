from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.speed("fastest")
        self.move_speed = 0.05

    def move(self):
        self.forward(10)

    def bounce(self):
        self.setheading(-self.heading())

    def paddle_bounce(self):
        # some formula I came up with, basically reflects heading direction
        self.setheading(self.heading() * 3)
        self.move_speed *= 0.9

    def refresh(self):
        self.setheading(self.heading() * 3)
        self.goto(0, 0)
        self.move_speed = 0.05