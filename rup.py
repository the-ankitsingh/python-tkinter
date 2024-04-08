import turtle

# Create a turtle object
rupee_turtle = turtle.Turtle()

# Set turtle properties
rupee_turtle.speed(1)  # Set the drawing speed (1 is slow, 10 is fast)
rupee_turtle.color("blue")  # Set the color of the drawing

# Draw the Indian Rupee symbol
rupee_turtle.penup()  # Lift the pen to move to the starting position
rupee_turtle.goto(0, 0)  # Move to the starting position
rupee_turtle.pendown()  # Lower the pen to start drawing

# Draw the vertical line
rupee_turtle.left(90)  # Turn the turtle 90 degrees to the left
rupee_turtle.forward(100)  # Draw the vertical line

# Draw the horizontal line
rupee_turtle.right(90)  # Turn the turtle 90 degrees to the right
rupee_turtle.forward(50)  # Draw the horizontal line

# Draw the two parallel lines
rupee_turtle.left(90)  # Turn the turtle 90 degrees to the left
rupee_turtle.forward(10)  # Move up slightly
rupee_turtle.left(90)  # Turn the turtle 90 degrees to the left
rupee_turtle.forward(100)  # Draw the first parallel line
rupee_turtle.left(90)  # Turn the turtle 90 degrees to the left
rupee_turtle.forward(10)  # Move down slightly
rupee_turtle.left(90)  # Turn the turtle 90 degrees to the left
rupee_turtle.forward(100)  # Draw the second parallel line

# Close the turtle graphics window on click
turtle.exitonclick()
