import turtle
from turtle import Turtle, Screen
import random

bekker = Turtle()
turtle.colormode(255)

bekker.hideturtle()


def draw_damian(distance):
    def colors():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        random_color = (r, g, b)
        return random_color

    def draw_a_dot():
        bekker.dot(20, colors())

    position_x = -350
    position_y = -255
    bekker.penup()

    bekker.goto(position_x, position_y)

    def one_line():
        amount = 0

        while amount < 13:
            bekker.forward(distance)
            draw_a_dot()
            amount += 1

    total_line = 11

    bekker.speed("fastest")

    while total_line > 0:
        one_line()
        total_line -= 1
        position_y += distance

        bekker.goto(position_x, position_y)


draw_damian(50)

hello = Screen()

hello.exitonclick()
