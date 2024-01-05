from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_lists = []
turtle_name = ["tim", "lam", "kam", 'jam', 'dam', 'fam']

for turtle in turtle_name:
    turtle = Turtle(shape="turtle")
    turtle_lists.append(turtle)

i = 0
y = -100

print(turtle_lists)

for list in turtle_lists: 
    list.color(colors[i])
    list.penup()
    list.goto(x=-230, y= y)
    y += 30
    i += 1
    
is_on = False 

if user_bet:
    is_on = True
    
while is_on:
    for list in turtle_lists:
        if list.xcor() > 230:
            is_on = False
            winner = list.pencolor()
            if winner == user_bet:
                print(f"You are the winner.")
            else:
                print(f"You lose. The {winner} color is winner.")
        dis = random.randint(0, 10)
        list.forward(dis)


screen.exitonclick()