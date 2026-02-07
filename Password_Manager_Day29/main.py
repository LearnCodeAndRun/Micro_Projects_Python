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

# Creating website label
website=Label(text="Website",fg="black",bg="#D3D3D3",highlightthickness=0,font=("Arial",10,"bold"))
website.grid(row=1,column=0)

# Creating website entry
website_entry=Entry(window,width=20)
website_entry.grid(row=1,column=0,columnspan=3)

# Creating email / username label
email=Label(text="Email / Username",bg="#D3D3D3",fg="black",font=("Arial",10,"bold"))
email.grid(row=2,column=0,padx=20)

# Creating email / username entry
email_entry=Entry(window,width=20)
email_entry.grid(row=2,column=0,columnspan=2)

# Creating password label
password=Label(text="Password",fg="black",bg="#D3D3D3",font=("Arial",10,"bold"))
password.grid(row=3,column=0)

# Creating password entry
password_entry=Entry(window,width=20)
password_entry.grid(row=3,column=0,columnspan=2)

# Creating generate password button
generate_password=Button(text="Generate Password",fg="black",bg="white",relief="raised",width=20)
generate_password.grid(row=3,column=1,padx=100)

# Creating add button
add_to_text=Button(text="Add",fg="black",width=20,bg="white",relief="raised")
add_to_text.grid(row=4,column=1,pady=20)
window.mainloop()