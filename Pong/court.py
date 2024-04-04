from turtle import Turtle
import random

class Court(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.draw_walls()
        self.draw_center_line()

    def draw_walls(self):
        self.penup()
        self.goto(-380, 270)
        self.pendown()
        for _ in range(2):
            self.forward(760)
            self.right(90)
            self.forward(540)
            self.right(90)
        self.penup()

    def draw_center_line(self):
        for position in range(240, -280, -40):
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.speed(random.randint(8, 10))
        segment.shapesize(2, 2, 1)
        segment.goto(random.randint(-300, 300), random.randint(-300, 300))
        segment.goto(0, position)
        segment.shapesize(0.5, 0.5, 1)
        self.segments.append(segment)
