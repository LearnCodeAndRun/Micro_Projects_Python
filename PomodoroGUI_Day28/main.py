# Building Pomodoro GUI using Tkinter
from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
tomato=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
text=Label(text="TIMER",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
start=Button(text="START",font=(FONT_NAME,15,"bold"))
reset=Button(text="RESET",font=(FONT_NAME,15,"bold"))
text.grid(column=1,row=0,padx=20,pady=20)
tomato.grid(column=0,row=1,columnspan=2)
start.grid(row=3,column=0,padx=20,pady=10)
reset.grid(row=3,column=1,padx=20,pady=10)
photo=PhotoImage(file="tomato.png")
tomato.create_image(100,112,image=photo)
window.mainloop()
