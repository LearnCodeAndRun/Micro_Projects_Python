from tkinter import *
from tkinter import messagebox as mb
from cryptography.fernet import Fernet
import os,random,pyperclip
import json

# ------------------------------PASSWORD KEY -------------------------------------#

def load_key():
    key_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"key.key")
    return open(key_path,"rb").read()

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
    final_password=''.join(password_list)
    password_entry.insert(0,final_password)
    pyperclip.copy(final_password)
    mb.showinfo('Success','Password copied to clipboard')

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_details():
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
    website_name=website_name.title()
    key=load_key()
    fernet=Fernet(key)
    encrypted_password=fernet.encrypt(password_details.encode()).decode()
    new_data={
        website_name:{
            "email":email_id,
            "password":encrypted_password
        }
    }
    data_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"data.json")
    try:
        with open(data_path,"r") as f:
            data=json.load(f)
    except FileNotFoundError:
        data={}
    data.update(new_data)
    with open(data_path,"w")as f:
        json.dump(data,f,indent=4)
    mb.showinfo(title="Success",message="Data saved successfully")
    website_entry.delete(0,END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)
    website_entry.focus()

# -------------------------- FIND PASSWORD -----------------------------#

def find_password():
    website_details=website_entry.get()
    if not website_details:
        mb.showerror(title="Empty",message="Write something in the website blank")
        return
    website_details=website_details.title()
    data_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"data.json")
    try:
        with open(data_path,"r") as f:
            data=json.load(f)
            key=load_key()
            fernet=Fernet(key)
            password=data[website_details]["password"]
            decrypted_password=fernet.decrypt(password.encode()).decode()
            mb.showinfo(title="Data found",message=f"Password for {website_details}: {decrypted_password}")
    except json.JSONDecodeError:
        mb.showerror(title="Empty JSON file",message="No website name found, file is empty")
    except FileNotFoundError:
        mb.showerror(title="No file exists",message="No data found")
    except KeyError:
        mb.showerror(title="Website Not Found",message="No such website name present")

# -------------------------KEY FILE CREATION----------------------------#

key_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"key.key")
if not os.path.exists(key_file):
    with open(key_file,"wb") as f:
        f.write(Fernet.generate_key())

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
website_entry=Entry(window,width=21)
website_entry.grid(row=1,column=1,sticky="EW")
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

# Creating search button
search=Button(text="Search",command=find_password,fg="black",bg="white",width=14,relief="raised")
search.grid(row=1,column=2,padx=(10,0),sticky="EW")

window.mainloop()