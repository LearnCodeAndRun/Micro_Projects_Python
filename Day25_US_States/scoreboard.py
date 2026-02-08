# Implementing the scoreboard
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.total_score=50
        self.color('black')
        self.penup()
        self.goto(-270,210)
        self.write(f"{self.score}/{self.total_score}",False,"center",("Arial",16,"normal"))
        self.color("white")
    def update_score(self):
        self.score+=1
        self.clear()
        self.color("black")
        self.write(f"{self.score}/{self.total_score}",False,"center",("Arial",16,"normal"))
        self.color("white")
    def check_score(self):
        if self.score==50:
            return False
        return True