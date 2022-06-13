from turtle import Screen, Turtle
from user_bar import UserBar
from computer_bar import ComputerBar
from Ball import Ball
from ScoreBoard import ScoreBoard
import time

Screen = Screen()
Screen.title("Pong")
Screen.bgcolor("black")
Screen.setup(width=600, height=600)
squares = []
user_bar = UserBar(squares)
user_bar.create_bar()

computer_bar = ComputerBar()

ball = Ball()

Screen.listen()
Screen.onkey(key="Up", fun=user_bar.move_up)
Screen.onkey(key="Down", fun=user_bar.move_down)
Screen.onkey(key="w", fun=computer_bar.move_up)
Screen.onkey(key="s", fun=computer_bar.move_down)

game_is_on = True

score = 0

user_score = ScoreBoard(-200, 200)
other_score = ScoreBoard(200, 195)
user_score.align = "right"
other_score.align = "left"
while game_is_on:
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(user_bar.head) < 50 or ball.distance(computer_bar) < 50:
        ball.bounce_x()
    if ball.xcor() > 295:
        user_score.score += 1
        user_score.update()
    elif ball.xcor() < -290:
        other_score.score += 1
        other_score.update()
    if ball.xcor() > 295 or ball.xcor() < -290:
        ball.hideturtle()
        ball.goto(0, 0)
        ball.y_move = 2
        ball.x_move = 2
        ball.showturtle()
        ball.bounce_x()
Screen.exitonclick()
