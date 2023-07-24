from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.hideturtle()
        self.score = 0
        self.goto(0, 265)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 20, "bold"))

