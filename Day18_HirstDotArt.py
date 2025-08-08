# Hirst painting project
import turtle,colorgram
import random
tup_color=colorgram.extract('HIRST PAINTING EXP.jpg',40)
color=[]
for i in tup_color:
    r=i.rgb.r
    g=i.rgb.g
    b=i.rgb.g
    color.append((r,g,b))
print(color)
turtle.colormode(255)
ob1=turtle.Turtle()
ob2=turtle.Screen()
ob1.penup()
ob1.setheading(225)
ob1.forward(300)
ob1.setheading(0)
for i in range(1,101):
    ob1.pendown()
    ob1.dot(20,random.choice(color))
    ob1.penup()
    ob1.forward(50)
    if i%10==0:
        ob1.setheading(90)
        ob1.forward(50)
        ob1.setheading(0)
        ob1.backward(500)
ob2.exitonclick()
