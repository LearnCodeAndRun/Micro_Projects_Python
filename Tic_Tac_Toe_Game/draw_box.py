# Draw the box
from turtle import Turtle
class Draw:
    def __init__(self):
        self.tim=Turtle("arrow")
        self.tim.color("azure")
    def draw_square(self):
        self.tim.penup()
        self.tim.goto(0,-150)
        self.tim.pendown()
        for i in range(0,5):
            if i==0 or i==4:
              self.tim.forward(150)
            else:
              self.tim.forward(300)
            self.tim.left(90) 
    def draw_lines(self):
       self.tim.penup()
       self.tim.goto(50,-150)
       self.tim.pendown()
       self.tim.goto(50,150)
       self.tim.penup()
       self.tim.goto(-50,150)
       self.tim.pendown()
       self.tim.goto(-50,-150)
       self.tim.penup()
       self.tim.goto(-150,-50)
       self.tim.pendown()
       self.tim.goto(150,-50)
       self.tim.penup()
       self.tim.goto(150,50)
       self.tim.pendown()
       self.tim.goto(-150,50)
       self.tim.penup()
       self.tim.hideturtle()
