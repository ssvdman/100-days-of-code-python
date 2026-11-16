import random
from turtle import Turtle, Screen

game_on = False
colors = ["red", "green", "blue", "orange", "yellow", "purple"]
screen = Screen()
screen.setup(width=500, height=500)
user_choice = screen.textinput(prompt="choose your turtle!", title="make a bet")

turtle_list = []
y_increment = 50
for i in range(6):
    tobj = Turtle("turtle")
    tobj.penup()
    tobj.color(colors[i])
    tobj.goto(-230, -150 + y_increment)
    y_increment += 50
    turtle_list.append(tobj)

if user_choice in colors:
    game_on = True
else:
    print("invalid bet")

while game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            game_on = False
            if user_choice == turtle.color():
                print(f"You won! {turtle.pencolor()} crossed the finish line first!")
            else:
                print(f"You lose! {turtle.pencolor()} crossed the finish line first!")
        turtle.forward(random.randint(1, 10))

screen.exitonclick()