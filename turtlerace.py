import turtle
from random import randint

# variable to compare distance traveled
tdis=0
t2dis=0
t3dis=0
t4dis=0

# creates turtles
screen = turtle.Screen()
ttrack = turtle.Pen()
ttrack.pencolor("white")
ttrack.shape("turtle")
t = turtle.Pen()
t.pencolor("red")
t.shape("turtle")
t2 = turtle.Pen()
t2.pencolor("blue")
t2.shape("turtle")
t3 = turtle.Pen()
t3.pencolor("orange")
t3.shape("turtle")
t4 = turtle.Pen()
t4.pencolor("purple")
t4.shape("turtle")

# creates track
turtle.screensize(400, 300, "black")
ttrack.penup()
ttrack.goto(-175, 75)
ttrack.pendown()
ttrack.goto(-175,-75)
ttrack.penup()
ttrack.goto(200,75)
ttrack.pendown()
ttrack.goto(200,-75)
ttrack.color("black")

# moves turtles to starting line
t.penup()
t.goto(-200,50)
t2.penup()
t2.goto(-200,25)
t3.penup()
t3.goto(-200,-25)
t4.penup()
t4.goto(-200,-50)

# loop that runs turtles until there is a winner
while t4dis < 375 or t3dis < 375 or t2dis < 375 or tdis < 375:
    a = randint(1,4)
    t.forward(a)
    tdis = tdis+a
    b = randint(1, 4)
    t2.forward(b)
    t2dis=t2dis+b
    c = randint(1,4)
    t3.forward(c)
    t3dis = t3dis + c
    d = randint(1, 4)
    t4.forward(d)
    t4dis = t4dis+d

# makes losing turtles disappear leaving the winner visible
if tdis < t2dis or tdis < t3dis or tdis < t4dis:
    t.pencolor("black")
if t2dis < tdis or t2dis < t3dis or t2dis < t4dis:
    t2.pencolor("black")
if t3dis < tdis or t3dis < t2dis or t3dis < t4dis:
    t3.pencolor("black")
if t4dis < tdis or t4dis < t2dis or t4dis < t3dis:
    t4.pencolor("black")

# exit on click
screen.exitonclick()