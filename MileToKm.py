# Mile to km converter using tkinter
from tkinter import *
root=Tk()
root.title("Mile to Km Converter")
root.minsize(400,300)
root.configure(bg="#0000FF")
lab1=Label(text="Welcome to Mile to Km Converter",bg="#F0F0F0",font=("Arial",16,"normal"),)
lab1.pack(pady=10)
lab2=Label(text="Enter distance in miles:",bg="#F0F0F0",font=("Arial",12,"normal"))
lab2.pack(pady=10)
ent=Entry(bg="#FFFFFF",width=20,relie="raised",font=("Arial",12,"normal"))
ent.pack(pady=10)
lab3=Label(text="Distance in kilometers will be shown here",bg="#F0F0F0",font=("Arial",12,"normal"))
lab3.pack(pady=10)
def miles_to_km():
    miles=float(ent.get())
    km=miles*1.60934
    lab3.config(text=f"Distance in kilometers: {km:0.4f} km")
submit=Button(text="Convert",bg="#00FF00",font=("Arial",12,"normal"),relief="sunken",command=miles_to_km)
submit.pack(pady=10)
root.mainloop()