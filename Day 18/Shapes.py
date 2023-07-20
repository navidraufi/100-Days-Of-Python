class Shapes:
    def __init__(self, shape):
        self.degree = 0
        self.shape = shape

    def draw(self, name_turtle, distance):
        degree = self.degree
        name_turtle.shape("triangle")
        if self.shape == "square":
            name_turtle.forward(distance)
            name_turtle.right(90)
            name_turtle.forward(distance)
            name_turtle.right(90)
            name_turtle.forward(distance)
            name_turtle.right(90)
            name_turtle.forward(distance)
        elif self.shape == "circle":
            degree = 0
            distanc = 1
            color = 1
            while degree < 28:
                name_turtle.forward(distanc)
                name_turtle.right(degree)
                name_turtle.color("red")
                degree += 1
                distanc += 1
                color += 1
        elif self.shape == "triangle":
            name_turtle.right(45)
            name_turtle.forward(100)
            name_turtle.right(135)
            name_turtle.forward(150)
            name_turtle.right(135)
            name_turtle.forward(100)
