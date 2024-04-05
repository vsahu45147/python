import turtle

# Create a screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the Sun
sun = turtle.Turtle()
sun.color("yellow")
sun.shape("circle")
sun.shapesize(2)  # Adjust size if needed

# Create planets
mercury = turtle.Turtle()
venus = turtle.Turtle()
earth = turtle.Turtle()
mars = turtle.Turtle()
jupiter = turtle.Turtle()
saturn = turtle.Turtle()
uranus = turtle.Turtle()
neptune = turtle.Turtle()

# Define planets' properties
planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
planet_colors = ["gray", "orange", "blue", "red", "brown", "yellow", "lightblue", "blue"]
planet_sizes = [0.2, 0.4, 0.5, 0.4, 1, 0.8, 0.7, 0.6]
planet_distances = [10, 20, 30, 40, 50, 100, 200, 300]

# Create planets in their orbits
for i in range(len(planets)):
    planets[i].color(planet_colors[i])
    planets[i].shape("circle")
    planets[i].shapesize(planet_sizes[i])
    planets[i].penup()
    planets[i].goto(planet_distances[i], 0)
    planets[i].pendown()

# Move planets in their orbits
for angle in range(3600):  # Increase angle for slower motion
    for i in range(len(planets)):
        planets[i].circle(planet_distances[i], 2)  # Increase the second parameter for slower motion

# Hide the turtle and display the result
for planet in planets:
    planet.hideturtle()
sun.hideturtle()

turtle.done()
