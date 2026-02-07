from tkinter import *
from tkinter import messagebox as mb
import os
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0,END)
    numbers=['0','1','2','3','4','5','6','7','8','9']
    letter=[chr(i) for i in range(65,91)]
    letter.extend([chr(i) for i in range(97,123)])
    symbols=['!','#','$','%','&','(',')','*','+']
    nr_letters=random.randint(8,10)
    nr_symbols=random.randint(2,4)
    nr_numbers=random.randint(2,4)
    password_list=[random.choice(letter) for _ in range(nr_letters)]
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])
    random.shuffle(password_list)
    final_password=""
    for i in password_list:
        final_password+=i
    password_entry.insert(0,final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_details():
    data_file=open('./Password_Manager_Day29/data.txt','a')
    website_name=website_entry.get()
    email_id=email_entry.get()
    password_details=password_entry.get()
    if not website_name or not email_id or not password_details:
        mb.showerror('Empty','Fill all details correctly')
        website_entry.delete(0,END)
        email_entry.delete(0,END)
        password_entry.delete(0,END)
        website_entry.focus()
        return
    check=mb.askokcancel("Check",f"Following has been noted:\nWebsite: {website_name}\nEmail ID: {email_id}\nPassword: {password_details}\nCheck whether all data are correct ?")
    if not check:
        website_entry.delete(0,END)
        email_entry.delete(0,END)
        password_entry.delete(0,END)
        website_entry.focus()
        return
    data_file.write(f"{website_name} | {email_id} | {password_details}\n")
    data_file.close()
    mb.showinfo(title="Success",message="Data saved successfully")
    website_entry.delete(0,END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)
    website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="#D3D3D3")

# Creating the canvas for logo
lock=Canvas(width=200,height=200,highlightthickness=0,bg="#D3D3D3")
lock_image= PhotoImage(file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"logo.png"))
lock.create_image(100,100,image=lock_image)
lock.grid(row=0,column=1,padx=20)

# Creating website label
website=Label(text="Website:",fg="black",bg="#D3D3D3",highlightthickness=0,font=("Arial",10,"bold"))
website.grid(row=1,column=0,sticky="EW")

# Creating website entry
website_entry=Entry(window,width=35)
website_entry.grid(row=1,column=1,columnspan=2,sticky="EW")
website_entry.focus()

# Creating email / username label
email=Label(text="Email / Username:",bg="#D3D3D3",fg="black",font=("Arial",10,"bold"))
email.grid(row=2,column=0,sticky="EW")

# Creating email / username entry
email_entry=Entry(window,width=35)
email_entry.grid(row=2,column=1,columnspan=2,sticky="EW")

# Creating password label
password=Label(text="Password:",fg="black",bg="#D3D3D3",font=("Arial",10,"bold"))
password.grid(row=3,column=0,sticky="EW")

# Creating password entry
password_entry=Entry(window,width=21)
password_entry.grid(row=3,column=1,sticky="EW")

# Creating generate password button
generate_password=Button(text="Generate Password",command=generate_password,fg="black",bg="white",relief="raised",width=14)
generate_password.grid(row=3,column=2,sticky="EW",padx=(10,0))

# Creating add button
add_to_text=Button(text="Add",command=save_details,fg="black",width=36,bg="white",relief="raised")
add_to_text.grid(row=4,column=1,columnspan=2,pady=20,sticky="EW")

window.mainloop()