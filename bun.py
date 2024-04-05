import turtle
import colorsys

screen = turtle.Screen()
screen.title('Colored Spiral of Spirals Fractal - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-100,-100,100,100)
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0)

def draw_spiral(x,y,length,direction):
    L = length
    c = 0
    
    color=colorsys.hsv_to_rgb((y+900)/1800,1,0.8)
    turtle.color(color)
    while length>1 or c<20:
        if length>2:
            draw_spiral(x,y,length*0.255,160+direction)
        
        turtle.up()
        turtle.seth(direction)
        turtle.goto(x,y)
        if length <=2:
            turtle.down()
            turtle.fd(length)
            x,y = turtle.xcor(),
            turtle.ycor()
            length *= 0.93
            direction += 20
            c += 1
            
        LL = 300
        draw_spiral(500,-500,LL,90)
        screen.update()
        ts=turtle.getscreen()
        ts.getcanvas().postscript(file = "spiral.eps")
        turtle.done()
        colorsys.done()
        
 