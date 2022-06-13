from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.goto(x=random.randint(-200, 200), y=random.randint(-200, 200))
        self.refresh()
    def refresh(self):
        self.goto(x=random.randint(-200, 200), y=random.randint(-200, 200))