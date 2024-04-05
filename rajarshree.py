from turtle import *
import colorsys
bgcolor('black')
pensize(4)
speed(0)
h=0
for i in range(150):
    color=colorsys.hsv_to_rgb(h,1,1)
    pencolor(color)
    h+=0.01
    circle(i,120)
    right(60)
    circle(i,-120)
done()