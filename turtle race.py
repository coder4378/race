#turtle race game
#importing required modules or library
import turtle
import random


#set up screen
screen = turtle.Screen()
screen.bgcolor("darkmagenta")
screen.title("turtle race")

#selection
favourite = input("select your player by color")
print("your player" , favourite)
print ("press space")

#draw border
border = turtle.Turtle()
border.color("yellow")
border.penup()
border.setposition(-300 , -300)
border.pendown()
border.pensize(5)

for side in range(4):
    border.forward(600)
    border.left(90)
    border.hideturtle()

#creating players
t_1 = turtle.Turtle()
t_1.color("white")
t_1.setheading(90)
t_1.penup()
t_1.pensize(3)
t_1.setposition(0 , -280)
t_1.pendown()

t_2 = turtle.Turtle()
t_2.color("lightgreen")
t_2.setheading(90)
t_2.penup()
t_2.pensize(3)
t_2.setposition(60 , -280)
t_2.pendown()

t_3 = turtle.Turtle()
t_3.color("lightblue")
t_3.setheading(90)
t_3.penup()
t_3.pensize(3)
t_3.setposition(-60 , -280)
t_3.pendown()

t_4 = turtle.Turtle()
t_4.color("lightpink")
t_4.setheading(90)
t_4.penup()
t_4.pensize(3)
t_4.setposition(120 , -280)
t_4.pendown()

t_5 = turtle.Turtle()
t_5.color("lightyellow")
t_5.setheading(90)
t_5.penup()
t_5.pensize(3)
t_5.setposition(-120 , -280)
t_5.pendown()

#movement
def move():
    y_1 = t_1.ycor()
    y_1 += random.randint(7 , 15)
    t_1.sety(y_1)
    y_2 = t_2.ycor()
    y_2 += random.randint(7 , 15)
    t_2.sety(y_2)
    y_3 = t_3.ycor()
    y_3 += random.randint(7 , 15)
    t_3.sety(y_3)
    y_4 = t_4.ycor()
    y_4 += random.randint(7 , 15)
    t_4.sety(y_4)
    y_5 = t_5.ycor()
    y_5 += random.randint(7 , 15)
    t_5.sety(y_5)

#key bindings
turtle.listen()
turtle.onkey(move , "space")
