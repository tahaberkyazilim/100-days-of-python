from turtle import Turtle
FONT = ("Courier", 24, "normal")

#Level & game over 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    def increase_score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER!", align = "center", font = FONT)

