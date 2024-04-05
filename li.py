import turtle as sm
import colorsys
sm.bgcolor("black")
sm.tracer(2)
sm.pensize(2)
h = 0

for i in range(190):
    color = colorsys.hsv_to_rgb
    h += 0.006
    sm.pencolor(color)
    sm.left(179)
    sm.backward(i*0.3)
    sm.circle(i*0.3,120)
    sm.right(14)
    sm.forward(i*0.2)
    sm.circle(i*.3,120)
sm.done()