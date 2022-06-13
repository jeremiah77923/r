from turtle import Turtle
import random
import time
class Car():
    def __init__(self):
        super().__init__()
        self.colors = ["red","yellow","green", "blue", "gold", "pink", "purple", "black", "tan"]
        self.cars = []
    def generate(self, level):
        random_chance = random.randint(1,6-level)
        nums = [1, 2, 3, 4, 5, 6,]
        if random_chance == 1:
            new_segment = Turtle()
            new_segment.hideturtle()
            new_segment.penup()
            new_segment.setx(300)
            new_segment.sety(random.randint(-260, 260))
            new_segment.showturtle()
            new_segment.shape("square")
            new_segment.shapesize(1, 2)
            new_segment.color(random.choice(self.colors))
            new_segment.forward(5*level)
            self.cars.append(new_segment)



