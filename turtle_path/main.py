from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=750, height=500)
FONT = ("Courier", 16, "normal")

cinema = Turtle()
mosque = Turtle()
home = Turtle()
message = Turtle()
message.hideturtle()

cinema.color("red")
mosque.color("green")

cinema.shape("circle")
mosque.shape("circle")

mosque.penup()
cinema.penup()

cinema.goto(100, 100)
mosque.goto(40, 50)

home.color("blue")
home.forward(40)
home.left(90)

while home.distance(mosque) >= 0:
    home.forward(1)
    if home.distance(mosque) == 0:
        break

home.right(90)
home.forward(60)
home.left(90)
home.forward(50)

message.penup()
message.goto(0, 200)
message.pendown()

if home.distance(cinema) < 40:
    message.write(f"You are there!! ", align="center", font=FONT)

else:
    message.write(f"Oops you are not there yet!!", align="center", font=FONT)

screen.exitonclick()
