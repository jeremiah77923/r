from turtle import Turtle


class User(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("blue")
        self.setheading(90)
        self.goto(0, -280)
    def move_up(self):
        self.forward(10)
    def move_right(self):
        self.right(90)
        self.forward(10)
    def move_left(self):
        self.left(90)
        self.forward(10)
    def move_down(self):
        self.backward(10)
    def reset(self):
        self.goto(0, -280)
        self.setheading(90)

