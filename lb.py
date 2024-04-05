import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Cricket LBW Simulation")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the cricket ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 250)
ball.dy = -1  # Initial downward speed

# Create the batsman
batsman = turtle.Turtle()
batsman.shape("square")
batsman.color("blue")
batsman.shapesize(stretch_wid=2, stretch_len=0.5)
batsman.penup()
batsman.goto(0, -250)

# Create the wicket
wicket = turtle.Turtle()
wicket.shape("square")
wicket.color("brown")
wicket.shapesize(stretch_wid=0.1, stretch_len=2)
wicket.penup()
wicket.goto(0, -260)

# Function to check if the ball hit the batsman's leg
def is_lbw():
    return ball.distance(batsman) < 20 and ball.ycor() < 0

# Main game loop
while True:
    screen.update()
    
    # Move the ball
    ball.sety(ball.ycor() + ball.dy)
    
    # Check for collision with the ground or batsman
    if ball.ycor() < -240 or is_lbw():
        ball.dy *= -1  # Reverse the direction
        
        # If LBW, change the ball color to green
        if is_lbw():
            ball.color("green")
            print("LBW! The batsman is out!")
            time.sleep(2)
            break
    
    time.sleep(0.01)

# Close the screen when done
screen.bye()
