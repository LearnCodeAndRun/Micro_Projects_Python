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
def reset_timer():
   global reps
   reps=-1
   window.after_cancel(timer)
   tomato.itemconfig(timer_text,text="00:00")
   text.config(text="TIMER",fg=GREEN)
   checkmark_emoji.grid_forget()
def count_down(count):
    global timer
    if count>=0:
      tomato.itemconfig(timer_text,text=f"{count//60:02d}:{count%60:02d}")
      timer=window.after(1000,count_down,count-1)
    else:
       start_timer()
def start_timer():
    global reps
    reps+=1
    if reps%8==0:
          text.config(text="LONG BREAK",fg=GREEN)
          reps=0
          mark=""
          for _ in range(4):
             mark+="✅"
          checkmark_emoji.config(text=mark)
          count_down(30)
    elif reps%2==0:
       mark=""
       for _ in range(reps//2):
         mark+="✅"
       text.config(text="SHORT BREAK",fg=PINK)
       checkmark_emoji.config(text=mark)
       checkmark_emoji.grid(column=1,row=3)
       count_down(10)
    else:
        if reps==1:
          checkmark_emoji.grid_forget()
        text.config(text="WORK TIME",fg=RED)
        count_down(20)
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
tomato=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
text=Label(text="TIMER",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
checkmark_emoji=Label(text="✅",bg=YELLOW,fg=RED,font=(FONT_NAME,20,"bold"))
start=Button(text="START",font=(FONT_NAME,15,"bold"),command=start_timer)
reset=Button(text="RESET",font=(FONT_NAME,15,"bold"),command=reset_timer)
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