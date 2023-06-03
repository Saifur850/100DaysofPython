import random
from turtle import Turtle

size = [0.5, 1.0]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.shape("circle")
        self.penup()

        self.color("blue")
        self.refresh()

    def refresh(self):
        x_ran = random.randint(-280, 280)
        y_ran = random.randint(-280, 280)
        self.goto(x_ran, y_ran)
        self.shape_size()

    def shape_size(self):
        ran_size = random.choice(size)
        self.shapesize(ran_size, ran_size)
        self.point = ran_size*2
