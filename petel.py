import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")

    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.color("red")
    flower.speed(2)

    # Draw the stem
    flower.penup()
    flower.goto(0, -200)
    flower.pendown()
    flower.pensize(5)
    flower.left(90)
    flower.forward(200)

    # Draw the petals
    petal_radius = 40
    for _ in range(36):
        flower.forward(petal_radius)
        flower.right(45)
        flower.forward(petal_radius)
        flower.right(135)
        flower.forward(petal_radius)
        flower.right(45)
        flower.forward(petal_radius)
        flower.right(135)

        flower.right(10)  # Rotate to draw the next petal

    window.exitonclick()

# Call the function to draw the rose flower
draw_flower()
