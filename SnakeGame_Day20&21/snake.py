from turtle import Turtle
class Snake:
    def __init__(self):
        self.lst=[None]*3
        self.pos=[(-10,0),(0,0),(10,0)]
        for i in range(len(self.lst)-1,-1,-1):
            self.lst[i]=Turtle("square")
            self.lst[i].speed("fastest")
            self.lst[i].penup()
            self.lst[i].shapesize(0.5,0.5)
            self.lst[i].color("white")
            self.lst[i].goto(self.pos[i])
    def move_forward(self):  
          for i in range(len(self.lst)-1,0,-1):
            self.lst[i].goto(self.lst[i-1].xcor(),self.lst[i-1].ycor())
          self.lst[0].forward(10)
    def move_up(self):
        if self.lst[0].heading()!=270:
            self.lst[0].setheading(90)
    def move_down(self):
        if self.lst[0].heading()!=90:
            self.lst[0].setheading(270)
    def move_left(self):
        if self.lst[0].heading()!=0:
            self.lst[0].setheading(180)
    def move_right(self):
        if self.lst[0].heading()!=180:
            self.lst[0].setheading(0)
    def refresh(self):
        x=self.lst[len(self.lst)-1].xcor()
        y=self.lst[len(self.lst)-1].ycor()
        for i in range(2):
          self.lst.append(Turtle("square"))
          self.lst[len(self.lst)-1].shapesize(0.5,0.5)
          self.lst[len(self.lst)-1].penup()
          self.lst[len(self.lst)-1].color("white")
          self.lst[len(self.lst)-1].goto(x,y)
    def check_wall(self):
        x=self.lst[0].xcor()
        y=self.lst[0].ycor()
        if abs(x)>=295 and (self.lst[0].heading()==0 or self.lst[0].heading()==180):
            self.lst[0].goto(-x,y)
        if abs(y)>=195 and (self.lst[0].heading()==90 or self.lst[0].heading()==270):
            self.lst[0].goto(x,-y)
    def check_collision(self):
        for i in range(1,len(self.lst)):
            if self.lst[0].distance(self.lst[i].xcor(),self.lst[i].ycor())<7:
                if self.lst[0].heading()!=self.lst[i].heading():
                   return False
        return True
