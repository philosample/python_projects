from turtle import Turtle
from random import Random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
SPEED_LOW = 8
SPEED_HIGH = 11
COLLISION_DISTANCE = 15

random = Random()

class Car:

    def __init__(self, lane_y, player_pos):
        self.positions = ((310, lane_y), (320, lane_y), (330, lane_y))
        self.segments = []
        self.collision = False
        self.car_speed = random.randint(SPEED_LOW, SPEED_HIGH)
        self.car_color = COLORS[random.randint(0,5)]
        for position in self.positions:
            self.add_segment(position)
        self.last_segment = self.segments[-1]


    def add_segment(self, position):
        segment = Turtle(shape="square", visible=False)
        segment.penup()
        segment.shapesize(0.9, 0.9, 1)
        segment.goto(600,600)
        segment.color(self.car_color)
        segment.goto(position)
        segment.setheading(180)
        segment.showturtle()
        self.segments.append(segment)
    

    def move(self, player_pos):
        self.collision = False
        for segment in self.segments:
            segment.forward(self.car_speed)
            if segment.distance(player_pos) < COLLISION_DISTANCE:
                    self.collision = True
   