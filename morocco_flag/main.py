from turtle import *

screen = Screen()
screen.setup(width=750, height=500)

flag_bg = Turtle()
star = Turtle()

star.hideturtle()


def draw_square(linecolor, width=200, height=100):
    flag_bg.color(linecolor)

    flag_bg.penup()
    flag_bg.goto(-150, -height)
    flag_bg.pendown()

    for i in range(4):
        flag_bg.forward(width)
        if i % 2 == 0:
            flag_bg.forward(height)
        flag_bg.left(90)
    flag_bg.hideturtle()


flag_bg.begin_fill()
draw_square('red', )
flag_bg.end_fill()

star.showturtle()
star.color("green")
star.width(2)
star.penup()
star.goto(45, 45 / 2)
star.pendown()

for _ in range(5):
    star.right(144)
    star.forward(90)
star.hideturtle()

screen.exitonclick()
