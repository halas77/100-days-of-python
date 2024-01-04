import turtle
from turtle import Screen
import random

# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()



# for i in range(3,10):
#     for j in range(i):
#         timmy.forward(100)
#         timmy.right(360/i)

# colors = [
#     "red",
#     "blue",
#     "green",
#     "yellow",
#     "orange",
#     "purple",
#     "pink",
#     "brown",
#     "black",
#     "white",
#     "cyan",
#     "magenta",
#     "gold",
#     "silver",
#     "navy",
#     "violet",
#     "maroon",
#     "teal",
#     "gray",
#     "lime"
# ]


# def draw_shapes(shape):
#     degree = 360/shape
#     timmy.color(random.choice(colors))
#     for _ in range(shape):
#         timmy.forward(100)
#         timmy.right(degree)
        
# for shape in range(3, 11):
#     draw_shapes(shape)


# degrees = [0, 90, 180, 270]

# timmy.speed(9)
# timmy.pensize(10)
# for _ in range(100):
#     colors = random_color()
#     timmy.pencolor(colors)
#     timmy.forward(20)
#     timmy.setheading(random.choice(degrees))


timmy = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r =random.randint(0, 255)
    g =random.randint(0, 255)
    b =random.randint(0, 255) 
    my_color = (r, g, b)
    return my_color

timmy.speed("fastest")
def draw_spiro(gap):
    for _ in range(int(360/gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

draw_spiro(5)
    
screen = Screen()
screen.exitonclick()
