import turtle
from turtle import Turtle, Screen
import random

mt = Turtle()
mt.pensize(20)
mt.hideturtle()
mt.speed("fastest")
turtle.colormode(255)
color_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88),
              (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45),
              (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106),
              (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

mt.penup()
mt.setheading(225)
mt.forward(300)
mt.setheading(0)
mt.pendown()
x_coordinate = mt.xcor()

for row in range(10):
    for column in range(10):
        mt.pendown()
        mt.dot(20, random.choice(color_list))
        mt.penup()
        mt.forward(50)
    mt.setx(x_coordinate)
    mt.sety(mt.ycor() + 50)

screen = Screen()
screen.exitonclick()

# import colorgram
# color_object = colorgram.extract("image.jpg", 30)
# color_list = []
# for Cobject in color_object:
#     r = Cobject.rgb.r
#     g = Cobject.rgb.g
#     b = Cobject.rgb.b
#     container_tuple = (r, g, b)
#     color_list.append(container_tuple)
# print(color_list)
