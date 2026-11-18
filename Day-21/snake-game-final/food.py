from turtle import Turtle
import random

# Food inherits from Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(0.5, 0.5)
        self.color("yellow")
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(randx, randy)
