from turtle import Turtle, Screen
from Shapes import Shapes

screen = Screen()

tom = Turtle()
tom.shape("turtle")

colors = ["red", "blue", "cyan", "brown", "DarkOrange", "azure", "bisque", "DarkOrchid", "DarkGrey", "DeepPink",
          "DarkViolet", "green"]

sides = 3


def shape(sidez, color):
    for _ in range(sidez):
        angle = 360 / sidez
        tom.forward(100)
        tom.right(angle)
        tom.color(colors[color])

color = 0
while sides < 13:
    shape(sides,color)
    sides += 1
    color += 1
screen.exitonclick()
