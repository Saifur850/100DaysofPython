import turtle
import random
import colorgram
from turtle import Turtle, Screen

# colors= colorgram.extract("image.jpg", 30)
#
# color_tup=[]
# for color in colors:
#     r= color.rgb.r
#     g= color.rgb.g
#     b = color.rgb.b
#     new_color= (r,g,b)
#     color_tup.append(new_color)
# print(color_tup)

color= [(207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

tim= Turtle()
turtle.colormode(255)
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for m in range(10):
    for n in range(10):
        tim.dot(20, random.choice(color))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    for n in range(10):
        tim.forward(50)
    tim.setheading(0)


screen= Screen()
screen.exitonclick()

