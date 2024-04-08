import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Colorful Spiral")
screen.bgcolor("black")

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the colorful spiral
for i in range(360):
    t.pencolor(colors[i % 6])
    t.forward(i)
    t.left(59)

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.done()
