from turtle import Turtle, Screen
from Shapes import Shapes
import random
screen = Screen()

tom = Turtle()
tom.shape("turtle")

colors = ["red", "blue", "cyan", "brown", "DarkOrange", "azure", "bisque", "DarkOrchid", "DarkGrey", "DeepPink",
          "DarkViolet", "green"]

shapes = ["triangle", "circle", "square"]

sides = 3
screen.bgcolor("black")

def shape(sidez, color):
    tom.shape(random.choice(shapes))
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
