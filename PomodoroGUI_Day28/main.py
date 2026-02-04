# Building Pomodoro GUI using Tkinter
import os
from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
reps = 0
timer = None
def start_timer():
    tomato.delete(timer_text)
    timer_text=tomato.create_text(100,130,text=f"25:00",fill="white",font=(FONT_NAME,35,"bold"))
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
tomato=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
text=Label(text="TIMER",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
start=Button(text="START",font=(FONT_NAME,15,"bold"),command=start_timer)
reset=Button(text="RESET",font=(FONT_NAME,15,"bold"))
text.grid(column=1,row=0)
text.config(padx=20,pady=20)
tomato.grid(column=1,row=1)
start.grid(row=2,column=0,padx=10,pady=10)
reset.grid(row=2,column=2,padx=10,pady=10)
img_path=os.path.join(BASE_DIR,"tomato.png")
photo=PhotoImage(file=img_path)
tomato.create_image(100,112,image=photo)
timer_text=tomato.create_text(100,130,text=f"00:00",fill="white",font=(FONT_NAME,35,"bold"))
window.mainloop()
