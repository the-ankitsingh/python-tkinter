from turtle import *

speed(2)
Screen().bgcolor("white")
penup()
goto(-20,-20)
pendown()
color("white")
begin_fill()
circle(150)
end_fill()

penup()
goto(-100,10)
pendown()
begin_fill()
right(165)
forward(100)
right(130)
forward(100)
end_fill()

color("green")
penup()
goto(-30,-10)
pendown()
begin_fill()
right(70)
circle(140)
end_fill()

color("green")
penup()
goto(-100,20)
pendown()
begin_fill()
right(160)
forward(80)
right(130)
forward(90)
end_fill()

color("white")
penup()
goto(40,40)
pendown()
begin_fill()
right(60)
circle(140,-90)
right(30)
circle(50,-50)
left(90)
forward(40)
right(90)
forward(20)
penup()
goto(40,40)
pendown()
right(150)
circle(50,50)
left(80)
forward(40)
left(90)
forward(20)
left(98.5)
circle(95,-90)
end_fill()

color("green")
width(2)
begin_fill()
circle(92,90)
end_fill()
left(135)
width(5)

penup()
forward(10)
pendown()
forward(60)

penup()
goto(-150,-100)
pendown()

hideturtle()

done()