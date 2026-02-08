import time,turtle
class Timer(turtle.Turtle):
    def __init__(self,time):
        super().__init__()
        self.seconds=time*60
        self.color('black')
        self.penup()
        self.goto(270,210)
        self.write(f'{self.seconds//60:02d}:{self.seconds%60:02d}',False,"center",("Arial",16,"normal"))
        self.color('white')
    def countdown(self):
        while self.seconds>0:
            min=self.seconds//60
            sec=self.seconds%60
            self.clear()
            self.color('black')
            self.write(f'{min:02d}:{sec:02d}',False,"center",("Arial",16,"normal"))
            self.color('white')
            time.sleep(1)
            self.seconds-=1
    def check(self):
        if self.seconds==0:
            return False
        return True