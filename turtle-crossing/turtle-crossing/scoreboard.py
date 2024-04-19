from turtle import Turtle
from random import Random

FONT = ("Consolas", 12, "bold")
LEVEL_POS = (-275, 275)
LIVES_POS = (-275, 250)
 
random = Random()

class Scoreboard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.hideturtle()
        self.restart = False
        self.screen = screen
        self.level = 1
        self.lives = 3
        self.penup()
        self.color("white")
        self.write_scoreboard()


    def next_level(self):
        self.level += 1
        self.write_scoreboard()

    
    def lost_life(self):
        self.lives -= 1
        self.write_scoreboard()

    
    def write_scoreboard(self):
        self.clear()
        self.goto(LEVEL_POS)
        self.write(f"Level: {self.level}", font=FONT, align="left")
        self.goto(LIVES_POS)
        self.write(f"Lives: {self.lives}", font=FONT, align="left")


    def write_game_over(self):
        self.screen.onkeypress(self.restart_game, "r")
        self.screen.listen()

        while not self.restart:
            font_size = 48
            self.goto(0, -50)
            self.color_change()
            font_size += random.randint(-5, 30)
            game_over_font = ("Consolas", font_size, "bold")
            self.write("GAME OVER", font=game_over_font, align="center")
            self.goto(0, random.randint(-100, 100))


    def restart_game(self):
        self.restart = True

        
    def color_change(self):
        r = random.randint(5, 255)
        g = random.randint(5, 255)
        b = random.randint(5, 255)
        self.color((r, g, b), (b, g, r))


    