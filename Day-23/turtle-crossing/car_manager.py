from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.shapesize(stretch_len= 2, stretch_wid=1)
        self.penup()
        self.setposition(x=310, y=random.randrange(start=-250, stop=250, step=30))
        self.fast = STARTING_MOVE_DISTANCE

    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * level))
