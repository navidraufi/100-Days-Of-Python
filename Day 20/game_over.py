from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

    def game_over(self, score):
        self.write(arg=f"Game over! Total Score: {score}", align=ALIGNMENT, font=FONT )
