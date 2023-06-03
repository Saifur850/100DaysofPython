import turtle
from turtle import Turtle, Screen
import random
color= ['red', 'blue', 'yellow', 'green', 'orange', 'brown']
position= [100, 60, 20, -20, -60, -100]

screen= Screen()
screen.setup(width= 500, height= 400)
all_turtles= []
for n in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[n])
    new_turtle.goto(x=-240, y=position[n])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="User's bet", prompt="Which turtle will win the race? Enter the color: ")

race_continue=True
while race_continue:
    for n in all_turtles:
        random_forward= random.randint(0,10)
        n.forward(random_forward)
        if n.xcor()>220:
            race_continue=False
            turtle_color= n.pencolor()
if turtle_color== user_bet.lower():
    print("You win")
else:
    print("You lose")


screen.exitonclick()