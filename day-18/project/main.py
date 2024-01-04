import turtle
from turtle import Screen, Turtle
import random


colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "cyan",
    "magenta",
    "gold",
    "silver",
    "navy",
    "violet",
    "maroon",
    "teal",
    "gray",
    "lime"
]



tim = Turtle()

tim.speed("fastest")
tim.dot(20, colors)

screen = Screen()
screen.exitonclick()