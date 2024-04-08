from sketchpy import canvas
import turtle
obj = canvas.sketch_from_svg("bholebaba.svg")
t=turtle.Turtle()
t.penup()
t.goto(-60 , 290)
t.pendown()
t.pencolor("#ff6600")
#t.write("Har Har Mahadev" , align="center", font=("Arial",50, "Bold"))
obj.draw()
t.hideturtle()
turtle.done()

