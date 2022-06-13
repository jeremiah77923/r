from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.align = ""
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(x, y)
        self.write(f"{self.score}", align="center", font=("Arial", 50, "normal"))

    def update(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Arial", 50, "normal"))
