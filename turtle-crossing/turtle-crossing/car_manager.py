from turtle import Turtle
from random import Random
from car import Car
from lane import Lane

LANE_Y_POS = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
POPULATION_RATE = 5

random = Random()

class CarManager:
    def __init__(self, player_pos):
        self.lanes = []
        self.player_pos = player_pos

    
    def build_lanes(self, player_pos):
        for lane_y in LANE_Y_POS:
            self.lanes.append(Lane(lane_y, player_pos))


    def automation(self, player_pos):
        self.collision = False
        for current_lane in self.lanes:
            if random.randint(1, POPULATION_RATE) == 1:
                current_lane.populate_car()

            if current_lane.cars:
                current_lane.move_cars(player_pos)
            
            if current_lane.collision:
                self.collision = True

        
    def game_over(self):
        pass