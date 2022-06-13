import turtle
import pandas

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
score = 0
states = data.state
correct_states = []
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(f"Correct States: {score}/{50}", "Enter a state that you have not guessed yet "
                                                                     "type \"q\" to quit?").title()
    guessed_states.append(answer_state)
    if answer_state == "Q":
        break
    if len(data[data["state"] == answer_state]) > 0:
        correct_states.append(answer_state)
        score += 1
        turtle_state = turtle.Turtle()
        turtle_state.hideturtle()
        turtle_state.penup()
        state_data = data[data.state == answer_state]
        turtle_state.goto(x=int(state_data.x), y=int(state_data.y))
        turtle_state.write(answer_state)
missing_states = [state for state in states if state not in correct_states]
missed_states = {"states": missing_states}
missed = pandas.DataFrame(missed_states)
missed.to_csv("missed_states.csv")
print("View the states you missed in the missed_states.csv file")

screen.exitonclick()
