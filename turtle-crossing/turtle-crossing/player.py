from turtle import Turtle, Screen
from random import Random

STARTING_POSITION = (0, -275)
LEFT_WALL = -275
RIGHT_WALL = 275
TOP_WALL = 250
BOTTOM_WALL = -275
MOVE_DISTANCE = 25

random = Random()

class Player(Turtle):
    def __init__(self, screen):
        super().__init__() 
        self.hideturtle()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.screen = screen
        self.screen.colormode(255)
        self.shapesize(0.7, 0.7, 1)
        self.reset_player()


    def reset_player(self):
        self.hideturtle()
        self.next_level = False
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.showturtle()


    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)
        if self.ycor() > TOP_WALL:
            self.next_level = True


    def dwn(self):
        self.setheading(270)
        if self.ycor() > BOTTOM_WALL:
            self.forward(MOVE_DISTANCE)


    def left(self):
        self.setheading(180)
        if self.xcor() > LEFT_WALL:
            self.forward(MOVE_DISTANCE)


    def right(self):
        self.setheading(0)
        if self.xcor() < RIGHT_WALL:
            self.forward(MOVE_DISTANCE)


    def color_change(self):
        r = random.randint(5, 255)
        g = random.randint(5, 255)
        b = random.randint(5, 255)
        self.color((r, g, b), (b, g, r))
