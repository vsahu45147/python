import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
flower_turtle = turtle.Turtle()
flower_turtle.speed(2)

# Function to draw a petal
def draw_petal(radius):
    flower_turtle.circle(radius, 60)
    flower_turtle.left(120)
    flower_turtle.circle(radius, 60)
    flower_turtle.left(120)

# Function to draw a flower
def draw_flower(num_petals, petal_radius):
    for _ in range(num_petals):
        draw_petal(petal_radius)
        flower_turtle.left(360 / num_petals)
draw_flower(6, 100)
flower_turtle.hideturtle()
screen.mainloop()
