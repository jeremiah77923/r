from turtle import Turtle, Vec2D
import random

class ComputerBar(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("blue")
        self.speed("fastest")
        self.goto(-270, 0)
        self.shapesize(stretch_len=1.5, stretch_wid=6.5)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(Vec2D(x=self.xcor(), y=new_y))

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(Vec2D(x=self.xcor(), y=new_y))
