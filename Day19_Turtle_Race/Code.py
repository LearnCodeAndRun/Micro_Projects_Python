import turtle,random,tkinter.messagebox as mb
def gen_ob(tur,i,j,k):
    tur[i]=turtle.Turtle("turtle")
    tur[i].color(j)
    tur[i].penup()
    tur[i].goto(-250,k)
tur=[0]*6
scr=turtle.Screen()
colors=['red','orange','blue','yellow','green','purple']
scr.setup(580,480)
scr.title("Turtle Race")
user_input=''
is_game_on=False
while user_input not in colors:
  try:
    user_input=scr.textinput("Welcome to Turtle Race Game !", "Choose your turtle colour among the following: red, orange, blue, yellow, green, purple").lower()
  except:
     print("No input has been provided")
     exit()
k=-200
for i in range(6):
    gen_ob(tur,i,colors[i],k)
    k+=80
i=0
while True:
   tur[i].forward(random.randint(0,10))
   if tur[i].xcor()>=270:
      break
   i=(i+1)%6
if tur[i].pencolor()==user_input:
   mb.showinfo("Result",f"Winner: {tur[i].pencolor().title()}. You chose: {user_input.title()}. Congratulations, you won !")
else:
   mb.showinfo("Result",f"Winner: {tur[i].pencolor().title()}. You chose: {user_input.title()}. Sorry, you lost ! Better luck next time...")
scr.exitonclick()
