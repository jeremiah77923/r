from turtle import Turtle


class Snake:
    def __init__(self, Squares):
        self.squares = Squares
        self.head = ""

    def create_snake(self):
        starting_positions = [(0, 0), (0, 0), (0, 0)]
        for position in starting_positions:
            self.add_segment(position)
        self.head = self.squares[0]

    def add_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.color("red")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.goto(position)
        self.squares.append(new_segment)
    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]
    def extend(self):
        self.add_segment(self.squares[-1].position())
    def move(self):
        for seg_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[seg_num - 1].xcor()
            new_y = self.squares[seg_num - 1].ycor()
            self.squares[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def home(self):
        for seg_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[seg_num - 1].xcor()
            new_y = self.squares[seg_num - 1].ycor()
            self.squares[seg_num].goto(x=new_x, y=new_y)
        self.squares[0].goto(0,0)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
