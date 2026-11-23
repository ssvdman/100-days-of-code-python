from turtle import Turtle
FONT = ("Arial Black", 20, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(x = -230, y = 255)
        self.level = 0
        self.score()

    def refresh(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def score(self):
        self.refresh()
        self.level += 1

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)
