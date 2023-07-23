import turtle
from turtle import Turtle, Screen
import random

bekker = Turtle()
turtle.colormode(255)


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = 0
radius = 100
bekker.speed("fastest")
while direction < 360:
    bekker.color(colors())
    bekker.circle(radius)
    bekker.setheading(direction)

    direction += 1
hello = Screen()

hello.exitonclick()
