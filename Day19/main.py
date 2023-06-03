from turtle import Turtle, Screen
tim= Turtle()
screen= Screen()

def move_forwards():
    tim.forward(20)

def move_upwards():
    tim.backward(20)

def turn_clockwise():
    tim.right(10)

def turn_anticlockwise():
    tim.left(10)

def clear():
    tim.speed(50)
    tim.penup()
    tim.home()
    tim.pendown()
    tim.clear()

screen.listen()
screen.onkey(move_forwards , "w")
screen.onkey(move_upwards , "s")
screen.onkey(turn_clockwise, "d")
screen.onkey(turn_anticlockwise, "a")
screen.onkey(clear, "c")

screen.exitonclick()