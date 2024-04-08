import turtle

screen=turtle.Screen()

screen.title("Colorful Spiral")

screen.bgcolor("black")

t=turtle.Turtle()
t.speed(0)
t.pensize(2)

colors=["red" , "orange" "green", "yellow",
        "blue", "purple", "pink"]

for i in range(360):
    t.pencolor(colors[i % 6])
    t.forward(1)
    t.left(59)

t.hideturtle()

turtle.done()
