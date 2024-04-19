from turtle import Turtle

FONT = ("Consolas", 12, "bold")
LEVEL_POS = (-275, 275)
LIVES_POS = (-275, 250)

class Scoreboard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.hideturtle()
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
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align="center")
