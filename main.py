from turtle import Turtle,Screen
from tkinter import messagebox as mb
from draw_box import Draw
from Turns import Play
scr=Screen()
scr.bgcolor("black")
scr.title("Tic-Tac-Toe")
a=None
while a!='X' and a!='O':
  a=scr.textinput("Start Game","\'X\' or \'O\'").upper()
  if a!='X' and a!='O':
    mb.showinfo("Error","Enter proper sign, \'X\' or \'O\' and nothing else")
obj=Draw()
obj.draw_square()
obj.draw_lines()
b=''
if a=='X':
  b='O'
else:
  b='X'
scr.listen()
use=Play(a,b,scr)
use.start()
scr.mainloop()