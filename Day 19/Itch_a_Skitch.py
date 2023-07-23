from turtle import Turtle, Screen

carl = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    carl.forward(10)


def move_back():
    carl.back(10)


def turn_right():
    position = carl.heading()
    position += 10

    carl.setheading(position)


def turn_left():
    position = carl.heading()
    position -= 10

    carl.setheading(position)


def clear():
    carl.goto(0, 0)
    carl.setheading(0)
    carl.clear()


screen.onkey(fun=move_forward, key="w")

screen.onkey(fun=move_back, key="s")

screen.onkey(fun=turn_right, key="d")

screen.onkey(fun=turn_left, key="a")

screen.onkey(fun=clear, key= "c")


screen.exitonclick()
