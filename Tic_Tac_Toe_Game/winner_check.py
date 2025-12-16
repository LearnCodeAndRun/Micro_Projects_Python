# Checking the winner
from turtle import Turtle
class Winner:
    def __init__(self):
        self.coordinates=[(-100,100),(0,100),(100,100),(-100,0),(0,0),(100,0),
                          (-100,-100),(0,-100),(100,-100)]
        self.list_for_entries=[None]*3
        self.winning_positions=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8)
                                (0,4,8),(2,4,6)]
        self.tim=Turtle()
    def click_handler(self,x,y):
        row,col=0,0
        if -150<=x<-50: col=0
        elif -50<=x<50: col=1
        elif 50<=x<=150: col=2
        else: return
        if -150<=y<-50: row=2
        elif -50<=y<50: row=1
        elif 50<=y<150: row=0
        else: return
        cell_index=row*3+col
        if 0<=cell_index<9 and self.list_for_entries[cell_index]==None:
            pass
    def check_winner_entry(self):
        if self.list_for_entries[0]["entry"]!=None:
            if self.list_for_entries[0]==self.list_for_entries[1]==self.list_for_entries[2]:
                pass
