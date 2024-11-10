from turtle import Turtle

ALIGN = "center"
FONT = ("Verdana", 10, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.score = 0
        self.show_updated_score()

    def show_updated_score(self):
        self.clear()
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)
    def increase_score(self):
        self.score += 1
        self.show_updated_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=("Verdana", 10, "normal"))