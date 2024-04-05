import turtle
forw = 1
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)

while True:
    t.forward(forw)
    t.color("yellow")
    t.left(120+23)
    t.left(1)
    forw += 1
    t.forward(forw)
    t.color("greenyellow")
    t.right(350)
    t.radians()
    t.color("orange")
    t.right(30)
    turtle.done()