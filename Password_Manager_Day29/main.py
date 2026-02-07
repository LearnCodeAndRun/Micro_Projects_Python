from tkinter import *
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20,bg="#D3D3D3")
# Creating the canvas for logo
lock=Canvas(width=200,height=200,highlightthickness=0,bg="#D3D3D3")
lock_image= PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"logo.png"))
lock.create_image(100,100,image=lock_image)
lock.grid(row=0,column=1,padx=20)
window.mainloop()