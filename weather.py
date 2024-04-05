import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Weather Animation")
screen.setup(width=600, height=600)
screen.bgcolor("lightblue")

# Create a turtle for the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.penup()
sun.goto(-250, 200)

# Create a turtle for the clouds
clouds = []
for _ in range(5):
    cloud = turtle.Turtle()
    cloud.shape("circle")
    cloud.color("white")
    cloud.penup()
    cloud.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(100, 250)
    cloud.goto(x, y)
    clouds.append(cloud)

# Create a turtle for the raindrops
raindrops = []
for _ in range(20):
    raindrop = turtle.Turtle()
    raindrop.shape("triangle")
    raindrop.color("blue")
    raindrop.penup()
    raindrop.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    raindrop.goto(x, y)
    raindrop.dy = random.uniform(-0.5, -1.5)
    raindrops.append(raindrop)

# Function to move the raindrops
def move_raindrops():
    for raindrop in raindrops:
        raindrop.sety(raindrop.ycor() + raindrop.dy)
        # If raindrop goes below the screen, reset its position
        if raindrop.ycor() < -300:
            raindrop.goto(random.randint(-300, 300), random.randint(-200, 200))

# Main animation loop
while True:
    move_raindrops()
    screen.update()
