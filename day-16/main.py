# from turtle import Turtle, Screen
# timmy  = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Childers", ["Dawit", "Beza", "Marta"])
table.add_column("Parents", ["Mellese", "Tsehay", "God almighty"])
table.align = "l"

print(table)






