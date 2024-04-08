import turtle
from random import *
from turtle import *

penup()
goto(-140,140)

for sp in range(15) :
    speed(15)
    write(sp)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

    ankit = Turtle()
    ankit.color('green')
    ankit.shape('turtle')
    ankit.penup()
    ankit.goto(-160,100)
    ankit.pendown()

    singh = Turtle()
    singh.color('red')
    singh.shape('turtle')
    singh.penup()
    singh.goto(-160,80)
    singh.pendown()

    turtlevar = Turtle()
    turtlevar.color('blue')
    turtlevar.shape('turtle')
    turtlevar.penup()
    turtlevar.goto(-160,60)
    turtlevar.pendown()


    
for turn in range(100): 
  ankit.forward(randint(1,5)) 
  singh.forward(randint(1,5)) 
  turtlevar.forward(randint(1,5)) 

turtle.done()