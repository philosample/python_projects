import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def game_init():
    scoreboard.__init__(screen)
    player.__init__(screen)
    car_manager.__init__(player.position())
    screen.onkeypress(player.up, "Up")
    screen.onkeypress(player.dwn, "Down")
    screen.onkeypress(player.left, "Left")
    screen.onkeypress(player.right, "Right")
    screen.listen()

    car_manager.build_lanes(player.position())


def screen_init():
    screen.clearscreen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Turtle Cross")
    screen.colormode(255)
    screen.tracer(0)
    

def game_state():
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
    screen_init()
    screen.tracer(1)
    scoreboard.write_game_over()
    game_is_on = False
    screen.onkeypress(restart_game, "r")
    screen.listen()

    # while not player.restart:
    #     car_manager.game_over()
    #     screen.update()
    #     time.sleep(0.1)    


def restart_game():
    main_game()


def main_game():
    screen_init()
    game_init()

    game_is_on = True
    level_speed = 0.1

    while game_is_on:
        player.color_change()
        car_manager.automation(player.position())
        game_state()
        time.sleep(level_speed)
        screen.update()


screen = Screen()
t = Turtle()
scoreboard = Scoreboard(screen)
player = Player(screen)
car_manager = CarManager(player.position())

main_game()

t.mainloop()
screen.exitonclick()