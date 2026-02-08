import turtle,pandas,time,scoreboard
from tkinter import messagebox as mb
data=pandas.read_csv('./Day25_US_States/50_states.csv')
dic=data.to_dict()
scr=turtle.Screen()
scr.title("US States Game")
scr.addshape('./Day25_US_States/blank_states_img.gif')
tim=turtle.Turtle()
tim.shape('./Day25_US_States/blank_states_img.gif')
start_time=time.time()
store_score=scoreboard.Score()
game_is_on=True
state_value={}
while game_is_on:
  name=scr.textinput('US State Name','Enter name of US State:')
  name=name.title()
  dic=data[data.state==name].to_dict()
  key=list(dic['state'].keys())
  print(key)
  if len(key)==0 or key[0] in state_value:
         mb.showinfo('Wrong','No city of that name exists or you have\n already entered that city')
         continue
  state_value[key[0]]=True
  obj=turtle.Turtle()
  obj.color('black')
  obj.penup()
  obj.goto(dic['x'][key[0]],dic['y'][key[0]])
  obj.write(dic['state'][key[0]],False,"center",("Arial",8,"normal"))
  obj.color('white')
  store_score.update_score()
  game_is_on=store_score.check_score()
scr.exitonclick()