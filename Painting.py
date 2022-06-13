"""
Created by Jeremiah Hawthorne
Created on Monday, June 30th, 2021
Finished on Monday, June 30th, 2021
Hirst Dot Painting created using the turtle module
"""

# import the turtle module to make the painting:
import turtle as turtle_module
# import the random module so we can have different colored dots:
import random
# Import the colorgram module to get access the image.jpg's color's
import colorgram

# Create a new turtle object called timmy:
timmy = turtle_module.Turtle()
# Set the pen up so lines on the screen do not appear:
timmy.pendown()
# Set the shape of the turtle to a turtle:
timmy.shape("turtle")
# Set the color mode to RGB:
turtle_module.colormode(255)
# Ask the user how fast they want to Turtle to go:
turtle_speed = input("How fast do you want the turtle to go? Type \"fastest\", \"slowest\", \"fast\", or \"slow\".\n")
# Set the turtle's speed based on the user's input:
timmy.speed(turtle_speed)
# List of colors from the image:
color_list = [(202, 109, 164), (238, 245, 240), (150, 49, 75), (223, 135, 201), (52, 124, 93), (172, 40, 154),
              (140, 19, 30), (133, 185, 163), (198, 71, 91), (46, 86, 122), (72, 35, 43), (145, 148, 178), (13, 71, 99),
              (233, 164, 175), (161, 158, 142), (105, 77, 74), (55, 50, 46), (183, 171, 205), (36, 74, 60),
              (18, 90, 86), (81, 129, 148), (148, 20, 17), (14, 64, 70), (30, 100, 68), (107, 153, 127), (174, 97, 94),
              (176, 209, 192), (227, 177, 173), (68, 58, 63), (111, 142, 140), (255, 0, 194), (178, 202, 196)]

# Setting the starting position of the turtle:
timmy.setheading(225)
timmy.forward(400)
timmy.setheading(0)


def paint():
    """ Paints a line of dots on the screen"""
    for x in range(12):
        # Make a dot on the screen with a random color from color_list:
        timmy.dot(20, random.choice(color_list))
        # Move timmy forward by 50 spots:
        timmy.forward(50)
    # Turn the timmy to the left:
    timmy.setheading(90)
    # Move timmy forward 50 points:
    timmy.forward(50)
    # Turn the turtle:
    timmy.setheading(180)
    # Move the turtle back at the same x coordinate as the last line but a little higher
    # than the last line to do a new line:
    timmy.forward(600)
    # Set the turtle around to draw the dots of the current line: 
    timmy.setheading(0)


# Paint 13 lines of randomly colored dots:
for x in range(13):
    # call the paint method to create a new line:
    paint()
# Create a new screen:
screen = turtle_module.Screen()
# Set the screen to exit on click:
screen.exitonclick()

"""
Created by Jeremiah Hawthorne
Created on Monday, June 30th, 2021
Finished on Monday, June 30th, 2021
Hirst Dot Painting created using the turtle module 
"""
