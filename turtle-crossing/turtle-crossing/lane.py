from car import Car
from random import Random

CAR_SPACING = 100

class Lane:


    def __init__(self, lane_y, player_pos):
        self.lane_y = lane_y
        self.player_pos = player_pos
        self.cars = []
        self.collision = False


    def populate_car(self):
        if not self.cars:
            self.cars.append(Car(self.lane_y, self.player_pos))
        else:
            if self.cars[-1].last_segment.xcor() < CAR_SPACING:
                self.cars.append(Car(self.lane_y, self.player_pos))


    def move_cars(self, player_pos):
        self.collision = False
        for car in self.cars:
            car.move(player_pos)
            if car.last_segment.xcor() < -310:
                self.cars.remove(car)
            if car.collision:                
                self.collision = True
                