import turtle

def colored_spiral(x, y, length, angle, colors, levels):
    if levels == 0:
        return
    else:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        color_index = levels % len(colors)
        turtle.color(colors[color_index])

        for _ in range(36):
            turtle.forward(length)
            turtle.left(angle)

        new_length = length * 0.9
        new_x = x + length * 0.9
        new_y = y + length * 0.9

        colored_spiral(new_x, new_y, new_length, angle, colors, levels - 1)

def main():
    turtle.speed(2)
    turtle.bgcolor("white")
    turtle.hideturtle()

    start_x = 0
    start_y = 0
    start_length = 10
    start_angle = 10
    start_levels = 5

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    colored_spiral(start_x, start_y, start_length, start_angle, colors, start_levels)

    turtle.done()

if __name__ == "__main__":
    main()
