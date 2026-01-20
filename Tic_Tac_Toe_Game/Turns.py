# Turns in the game
from turtle import Turtle
from tkinter  import messagebox as mb
import random
class Play:
    def __init__(self,symbol,computer_symbol,screen):
        self.screen=screen
        self.visited=[None]*9
        self.winning_positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.marking={0:(-100,100),1:(0,100),2:(100,100),3:(-100,0),4:(0,0),5:(100,0),6:(-100,-100),7:(0,-100),8:(100,-100)}
        self.user_symbol=symbol
        self.computer_symbol=computer_symbol
        self.turn=None
        self.game_is_on=True
        self.tim=Turtle()
        self.tim.penup()
        self.tim.color('white')
        self.tim.hideturtle()
    def start(self):
        self.screen.onclick(self.pinpoint_index_user_turn)
        if self.user_symbol=='X':
            self.turn='USER'
        else:
            self.turn='COMPUTER'
        if self.turn=='COMPUTER':
            self.choose_cell_computer_turn()
    def pinpoint_index_user_turn(self,x,y):
        if self.turn!='USER':
            return
        row,column,position=-1,-1,-1
        if -150<=x<-50:
            column=0
        elif -50<=x<50:
            column=1
        elif 50<=x<100:
            column=2
        else:
            return
        if -150<=y<-50:
            row=2
        elif -50<=y<50:
            row=1
        elif 50<=y<150:
            row=0
        else:
            return
        position=row*3+column
        if self.visited[position]==None:
          self.visited[position]=self.user_symbol
          self.tim.goto(self.marking[position])
          self.tim.write(self.user_symbol,False,"center",("Arial",16,"normal"))
        self.game_is_on=self.check_winner()
        if not self.game_is_on:
            return
        self.turn='COMPUTER'
        self.choose_cell_computer_turn()
    def choose_cell_computer_turn(self):
        if self.turn!='COMPUTER':
            return
        while True:
          position=random.randint(0,8)
          if self.visited[position]==None:
              self.visited[position]=self.computer_symbol
              self.tim.goto(self.marking[position])
              self.tim.write(self.computer_symbol,False,"center",("Arial",16,"normal"))
              self.game_is_on=self.check_winner()
              if not self.game_is_on:
                return
              self.turn='USER'
              break
    def check_winner(self):
        for i in self.winning_positions:
            if self.visited[i[0]]!=None and self.visited[i[0]]==self.visited[i[1]]==self.visited[i[2]]:
                winning_symbol=self.visited[i[0]]
                if winning_symbol==self.computer_symbol:
                    mb.showinfo("Result","Computer won ! Better luck, next time")
                else:
                    mb.showinfo("Result","Congratulations, you won !")
                return False
        return True