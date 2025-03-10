import turtle
from random import randint, randrange
from turtle import Turtle, Screen
import random

"""Random direction choices"""
random_dir_choice = [0,90,180,270]

"""Set timmy as Turtle()"""
timmy = Turtle()

"""Use 0-255 colour space"""
turtle.colormode(255)

"""Set pen thickness"""
timmy.pensize(10)

walk = True
while walk:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    timmy.color(r,g,b)
    timmy_choice = randrange(0,4)

    timmy.forward(20)
    timmy.right(random_dir_choice[timmy_choice])

screen = Screen()
screen.exitonclick()
