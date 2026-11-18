from inspect import FullArgSpec
from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align= ALIGN, font= FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)

