import turtle as t
import random
import tkinter as tk
import time

user_name = input("Hello what is your name?\n")
print(f"Welcome to Etch a Sketch {user_name}.")
time.sleep(1)
print("Controls:")
time.sleep(1)
print(f"To go forward, press the up arrow\nto  go backwards, press the down arrow \nto go left, press the left arrow "
      f"\nto go right, press the right arrow \nto clear the screen, press \"f\", \nto exit click on the x button on "
      f"the top "
      f"left or click on the screen.")
time.sleep(4)
timmy = t.Turtle()
timmy.shape("turtle")


def fowards():
    timmy.forward(25)


def backwards():
    timmy.back(25)



def right():
    timmy.right(20)


def left():
    timmy.left(20)


def clear():
    t.resetscreen()


screen = t.Screen()
screen.listen()
screen.title("Etch a Sketch")
screen.onkey(key="Up", fun=fowards)
screen.onkey(key="Down", fun=backwards)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)
screen.onkey(key="f", fun=clear)
screen.exitonclick()
