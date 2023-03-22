from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=500)
screen.title("Turtle Practice Session")

tim = Turtle()

tim.pen(pencolor="red", fillcolor="green")
tim.hideturtle()
tim.begin_fill()
tim.forward(200)
tim.goto(0, 200)
tim.home()
tim.end_fill()

screen.listen()
screen.onkey(tim.undo, "Up")

screen.exitonclick()
