from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.xpos = 0
        self.snake_segment = []
        self.create_snake()
        self.head = self.snake_segment[0]
    # make the snake
    # square dimension 20x20
    def create_snake(self):
        for i in range(3):
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.setx(self.xpos)
            self.xpos -= 20
            self.snake_segment.append(segment)

    #each segment now follows the head
    #range(start= tail of snake, end= head of snake, step=-1)
    def move(self):
        for seg_num in range(len(self.snake_segment) - 1, 0, -1):
            new_x = self.snake_segment[seg_num - 1].xcor()
            new_y = self.snake_segment[seg_num - 1].ycor()
            self.snake_segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)