from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.random_x = random.randint(-270, 270)
        self.random_y = random.randint(-270, 270)
        self.goto(self.random_x, self.random_y)

    def food_eaten(self):
        self.random_x = random.randint(-270, 270)
        self.random_y = random.randint(-270, 270)
        self.goto(self.random_x, self.random_y)
