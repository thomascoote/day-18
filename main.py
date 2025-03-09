import turtle
from random import randint
from turtle import Turtle, Screen
import random

def shape(sides):
    total_angle = (sides-2)*180
    return 180 - (total_angle/sides)


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
turtle.colormode(255)

print(shape(3))

##TODO 3 to 10 sided shapes, random colour, 100 length per side, all overlaid --- (n-2)*180



for sides in range (3,11):
    print(f"Next shape has {sides} sides")
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    i = sides
    timmy.color(r,g,b)
    while i > 0:
        turn_angle = shape(sides)
        timmy.right(turn_angle)
        timmy.forward(100)
        i -= 1

screen = Screen()
screen.exitonclick()
