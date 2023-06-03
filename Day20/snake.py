from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(position)
        self.segment.append(new_square)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def reset(self):
        for segment in self.segment:
            segment.goto(700, 700)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]


    def move(self):
        for squ_number in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[squ_number - 1].xcor()
            new_y = self.segment[squ_number - 1].ycor()
            self.segment[squ_number].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
