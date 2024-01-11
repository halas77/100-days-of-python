import turtle
import pandas
 
screen = turtle.Screen()
screen.title("State Game")
image = "./blank_states_img.gif" 
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
data_list = data.state.to_list()

count = 0

while count != 50:
    answer = screen.textinput(title=f"{count}/50 State", prompt="What's another state's name? ").capitalize()
    if answer in data_list:
        correct_answer = data[data["state"] == answer]
        new_tur = turtle.Turtle()
        new_tur.hideturtle()
        new_tur.penup()
        new_tur.goto(int(correct_answer.x), int(correct_answer.y))
        new_tur.write(answer)
        count += 1


screen.exitonclick()