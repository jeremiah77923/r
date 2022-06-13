from turtle import Turtle, Screen
from Cars import Car
import time
from User import User
from ScoreBoard import Score
screen = Screen()
screen.title("Crossy Road")
screen.listen()
screen.setup(600, 600)
car = Car()
screen.tracer(0)
count = 0
user = User()
screen.onkey(key="Up", fun=user.move_up)
screen.onkey(key="Right", fun=user.move_right)
screen.onkey(key="Left", fun=user.move_left)
screen.onkey(key="Down", fun=user.move_down)
level_num = 1
score = Score()
score.update(level_num)
while True:
    time.sleep(.1)
    screen.update()
    car.generate(level_num)
    for seg in car.cars:
        seg.backward(5*level_num)
        if user.distance(seg) <= 20:
            user.reset()
    if user.ycor() > 280:
        user.reset()
        level_num += 1
        score.update(level_num)
screen.exitonclick()
