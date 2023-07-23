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


bekker.pensize(15)
bekker.speed("fastest")

directions = [0, 90, 180, 270]

for _ in range(300):
    bekker.color(colors())
    bekker.forward(30)
    bekker.setheading(random.choice(directions))

hello = Screen()

hello.exitonclick()
