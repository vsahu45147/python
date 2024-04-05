import turtle
import math

# Function to draw a colored spiral
def draw_colored_spiral(radius, angle, color):
    turtle.color(color)
    for _ in range(90):
        turtle.forward(radius)
        turtle.right(angle)

# Function to draw a spiral of spirals
def draw_spiral_of_spirals(num_spirals, initial_radius, angle, color_list):
    for i in range(num_spirals):
        draw_colored_spiral(initial_radius, angle, color_list[i % len(color_list)])
        initial_radius += 10  # Increase radius for the next spiral

# Set up turtle window
turtle.bgcolor("black")
turtle.speed(0)  # Set the turtle speed to the maximum

# Define parameters
num_spirals = 10
initial_radius = 10
angle = 90
color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw the spiral of spirals
draw_spiral_of_spirals(num_spirals, initial_radius, angle, color_list)

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
