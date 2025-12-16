from turtle import Turtle,Screen
from draw_box import Draw
from winner_check import Winner
tim=Turtle()
tim.color("azure")
scr=Screen()
a=scr.textinput("Start Game","\'X\' or \'O\'").upper()
scr.bgcolor("black")
scr.title("Tic-Tac-Toe")
obj=Draw()
obj.draw_square()
obj.draw_lines()
win=Winner()
scr.listen()
scr.onscreenclick(win.click_handler)
game_is_on=True
scr.exitonclick()
