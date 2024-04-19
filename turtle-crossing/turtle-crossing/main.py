import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def game_init():
    global game_is_on, level_speed
    scoreboard.__init__(screen)
    player.__init__(screen)

    # for car in car_manager.lanes.cars:
    #     car.clear()

    car_manager.__init__(player.position())

    screen.onkeypress(player.up, "Up")
    screen.onkeypress(player.dwn, "Down")
    screen.onkeypress(player.left, "Left")
    screen.onkeypress(player.right, "Right")
    screen.listen()
    game_is_on = True
    level_speed = 0.1


def screen_init():
    screen.clearscreen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Turtle Cross")
    screen.colormode(255)
    screen.tracer(0)


def build_lanes():
    car_manager.build_lanes(player.position())


def automation():
    player.color_change()
    car_manager.automation(player.position())
    time.sleep(level_speed)
    screen.update()


def game_state():
    global level_speed
    if car_manager.collision:
        player.reset_player()
        scoreboard.lost_life()
        
        if scoreboard.lives == 0:
            game_over()

    elif player.next_level:
        scoreboard.next_level()
        player.reset_player()
        level_speed *= 0.8


def game_over():
    global game_is_on
    screen_init()
    screen.tracer(10)
    scoreboard.write_game_over()
    game_is_on = False


def main_game():
    screen_init()
    game_init()
    build_lanes()

    while game_is_on:
        automation()
        game_state()
        if scoreboard.restart:
            main_game()


screen = Screen()
screen_init()
t = Turtle()
scoreboard = Scoreboard(screen)
player = Player(screen)
car_manager = CarManager(player.position())
game_is_on = True
level_speed = 0.1

main_game()

screen.exitonclick()
t.mainloop()
