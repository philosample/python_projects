from turtle import Turtle

FONT = ("Consolas", 48, "bold")
PLAYER_SCORE_POS = (-220, 260)
COMP_SCORE_POS = (170, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.comp_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write_scores()

    def add_score(self, side):
        if side == "player":
            self.player_score += 1
        if side == "comp":
            self.comp_score += 1
        self.write_scores()

    def write_scores(self):
        self.clear()
        self.write_score(PLAYER_SCORE_POS, self.player_score)
        self.write_score(COMP_SCORE_POS, self.comp_score)

    def write_score(self, position, score):
        self.goto(position)
        self.write(score, font=FONT)
