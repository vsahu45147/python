import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightpink")  # Background color

# Set up the turtle
rose = turtle.Turtle()
rose.shape("turtle")
rose.color("red")  # Rose color
rose.speed(0)  # Set the fastest speed

# Draw a rose
for _ in range(36):
    rose.forward(100)
    rose.right(90)
    rose.forward(30)
    rose.right(90)
    rose.forward(100)
    rose.right(90)
    rose.forward(30)
    rose.right(90)
    rose.right(10)  # Rotate the turtle for the next petal

# Add a message
message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(0, -200)  # Position the message turtle
message_turtle.color("darkred")  # Message color
message_turtle.write("Happy Rose Day!", align="center", font=("Arial", 24, "bold"))

# Keep the window open
screen.mainloop()
