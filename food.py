from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.penup()
        self.speed("slowest")
        self.refresh()

    def refresh(self):
        self.random_x = random.randint(-280,280)
        self.random_y = random.randint(-280,280)
        self.goto(self.random_x, self.random_y)