# Displaying the scoreboard
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,170)
        self.sums=0
        self.write(f"Score: {self.sums}",False,"center",("Arial",16,"normal"))
        self.color("black")
    def refresh(self):
        self.sums+=3
        self.clear()
        self.color("white")
        self.write(f"Score: {self.sums}",False,"center",("Arial",16,"normal"))
        self.color("black")
