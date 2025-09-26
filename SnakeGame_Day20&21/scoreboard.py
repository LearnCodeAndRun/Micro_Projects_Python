# Displaying the scoreboard
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,filepath):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(-90,140)
        self.penup()
        self.high_score_record=Turtle()
        self.high_score_record.penup()
        self.high_score_record.color("white")
        self.high_score_record.goto(90,140)
        self.sums=0
        self.file=filepath
        with open(self.file,"r") as f:
           self.high_score=int(f.read())
        self.write(f"Score: {self.sums}",False,"center",("Arial",16,"normal"))
        self.high_score_record.write(f"High Score: {self.high_score}",False,"center",("Arial",16,"normal"))
        self.high_score_record.color("black")
        self.color("black")
    def refresh(self):
        self.sums+=3
        self.clear()
        self.color("white")
        self.write(f"Score: {self.sums}",False,"center",("Arial",16,"normal"))
        self.color("black")
        if self.sums>self.high_score:
            self.high_score=self.sums
            with open(self.file,"w") as f:
               f.write(f"{self.high_score}")
               f.seek(0)
    def display_high_score(self):
        with open(self.file,"r") as f:
          self.high_score=int(f.read())
        self.high_score_record.clear()
        self.high_score_record.color("white")
        self.high_score_record.write(f"High Score: {self.high_score}",False,"center",("Arial",16,"normal"))
