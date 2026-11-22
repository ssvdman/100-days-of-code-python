from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.setpos(x=xcor, y=0)

    def move_up(self):
        self.forward(20)
    def move_down(self):
        self.forward(-20)
