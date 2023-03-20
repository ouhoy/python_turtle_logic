from turtle import *

screen = Screen()
screen.setup(width=750, height=500)

flag_bg = Turtle()
star = Turtle()

flag_bg.penup()
flag_bg.goto(-200, -120)
flag_bg.pendown()


def draw_square(linecolor, length=200):
    flag_bg.color(linecolor)
    for i in range(4):
        flag_bg.forward(length)
        if i % 2 == 0:
            flag_bg.forward(100)
        flag_bg.left(90)


flag_bg.begin_fill()
draw_square('red')
flag_bg.end_fill()

star.color("green")
star.width(2)

for _ in range(5):
    star.right(144)
    star.forward(90)

screen.exitonclick()
