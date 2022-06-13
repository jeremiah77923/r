from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-240, 265)
        self.write(arg=f"Level: {self.score}", align="center", font=("Arial", 30, "normal"))

    def update(self, score):
        self.clear()
        self.write(arg=f"Level: {score}", align="center", font=("Arial", 30, "normal"))

