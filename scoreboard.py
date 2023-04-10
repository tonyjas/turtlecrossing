from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 1
        self.update_scoreboard()

    def increment(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! Score: {self.level}", False, align="center", font=FONT)
