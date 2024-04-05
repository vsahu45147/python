import turtle
#clcoding.com
t=turtle.Turtle()
s=turtle.Screen()
turtle.bgcolor("black")
t.speed(50)
for i in range(100):
    for i in range(40):
        t.pu()
        t.goto(10,100)
        t.pd()
        t.color("red")
        t.pensize(2)
        t.circle(150,steps=1000)
        t.right(10)
#youtube.com/castorclasses