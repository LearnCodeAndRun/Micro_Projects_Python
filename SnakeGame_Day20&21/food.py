# Code for food for the snake
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        random_tup=(random.randint(-280,280),random.randint(-180,180))
        self.goto(random_tup)
    def refresh(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-180,180)
        self.goto(random_x,random_y)
