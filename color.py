import turtle

t=turtle.Turtle()
turtle.setup(width=700,height=700)
t.speed(10)
colors=['purple','red','green','blue','yellow']
turtle.bgcolor('lightgrey')

for i in range(200):
    t.color(colors[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(72)