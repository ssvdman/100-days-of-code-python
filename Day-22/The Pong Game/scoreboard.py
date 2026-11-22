from turtle import Turtle
ALIGN = "center"
FONT = ('FONT', 50, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.setpos(0, 230)
        self.write(":", align=ALIGN, font=FONT)
        self.setpos(-50, 230)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.setpos(50, 230)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update()
    def r_point(self):
        self.r_score += 1
        self.update()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)