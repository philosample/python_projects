from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.ball_reset()
        self.x = 0
        self.y = 0
        self.ball_pos = (self.x, self.y)

    def move(self):
        self.forward(1)
        self.x = int(self.xcor())
        self.y = int(self.ycor())
        self.ball_pos = (self.x, self.y)

    def ball_reset(self):
        self.setheading(random.randint(135, 225))
        if self.heading() == 180:
            self.setheading(self.heading() + random.randint(10, 20))
        self.goto(0, 0)
