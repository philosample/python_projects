from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from court import Court
import time
import random

LEFT_WALL = -370
RIGHT_WALL = 370
TOP_WALL = 255
BOTTOM_WALL = -253
RANDOM_MIN = -20
RANDOM_MAX = 20
COMP_DISTANCE = 10
PLAYER_DISTANCE = 20
DOWN = 270
UP = 90


def wall_collision(ball_pos):
    x = ball_pos[0]
    y = ball_pos[1]
    if x < LEFT_WALL:
        scoreboard.add_score("comp")
        ball.ball_reset()
    if x > RIGHT_WALL:
        scoreboard.add_score("player")
        ball.ball_reset()
    if y >= TOP_WALL or y <= BOTTOM_WALL:
        bounce("wall", 1)
        return True
    else:
        return False


def paddle_collision(paddle, angle_mult):
    collision = False
    i = 1
    for segment in paddle.segments:
        if ball.distance(segment) < 19 and not collision:
            if paddle.paddle_type == "player":
                angle_mult = 0.99 - (i * 0.01)
            elif paddle.paddle_type == "comp":
                angle_mult = 1.01 - (i * 0.01)
            bounce("paddle", angle_mult)
            collision = True
        i += 1
    return collision


def bounce(col_type, angle_mult):
    current_direction = ball.heading()
    new_direction = 0
    if col_type == "wall":
        new_direction = 360 - current_direction
    elif col_type == "paddle":
        if current_direction < 180:
            new_direction = int(angle_mult * (180 - current_direction))
        elif current_direction <= 360:
            new_direction = int(angle_mult * ((360 - current_direction) + 180))
    if 20 < new_direction < 340:
        new_direction += random.randint(RANDOM_MIN, RANDOM_MAX)
    ball.setheading(new_direction)
    ball.forward(1)
    screen.update()
    print(f"current_direction: {current_direction}")
    print(f"new_direction {new_direction} ")
    print(f"angle_mult: {angle_mult}")


def move_ball():
    for _ in range(5):
        ball.move()
        screen.update()
        # time.sleep(0.1)


screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(1)
court = Court()
paddles = [Paddle('player'), Paddle('comp')]
player_paddle = paddles[0]
computer_paddle = paddles[1]
ball = Ball()
scoreboard = Scoreboard()
screen.tracer(0)

screen.listen()
screen.onkeypress(player_paddle.up, "Up")
screen.onkeypress(player_paddle.down, "Down")
game_is_on = True
paddle_bounce_delay = False

while game_is_on:
    screen.update()
    computer_paddle.comp_paddle_automation()
    move_ball()
    time.sleep(0.01)
    # print(ball.ball_pos)
    wall_collision(ball.ball_pos)
    screen.update()
    if -340 < ball.x < -300 or 300 < ball.x < 340:
        for paddle in paddles:
            if paddle_collision(paddle, angle_mult=1) and not paddle_bounce_delay:
                paddle_bounce_delay = True
    else:
        paddle_bounce_delay = False

screen.exitonclick()
