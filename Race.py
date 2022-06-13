import turtle as t
import random

screen = t.Screen()
screen.title("Turtle Racing")

screen.setup(width=500, height=400)
colors = ["blue", "red", "green", "yellow", "black", "gray", "pink", "gold"]
turtles = []
for color in colors:
    new_turtle = t.Turtle()
    new_turtle.color(color)
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.shape("turtle")
    turtles.append(new_turtle)
y = 180
for turtle in turtles:
    turtle.goto(-230, y)
    y -= 50
user_bet = screen.textinput("Place a bet", "What color turtle do you think will win?"
                            "Whichever color turtle is first at the end of the screen wins.").lower()


def check_bet(bet, winner):
    if winner[0] == bet:
        return f"You bet right! {winner[0]} won!!"
    return f"{winner[0]} won, but since {bet} did not win you loose. Better luck next time."


winner = ""


def at_end():
    global winner
    for turtle in turtles:
        if turtle.xcor() >= 225:
            winner = turtle.color()
            return True
        elif turtle.xcor() < 225:
            turtle.forward(random.randint(1, 10))
    return False


winner = ""
while at_end() == False:
    if at_end():
        break
count = 0
print(check_bet(bet=user_bet, winner=winner))

screen.exitonclick()
