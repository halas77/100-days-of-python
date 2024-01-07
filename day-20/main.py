from turtle import Turtle, Screen
from snake import Snake 
from food import Food 
from scoreboard import ScoreBoard 
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_on = True

while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.segemnts[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.segemnts[0].xcor() > 280 or snake.segemnts[0].xcor() < -280 or snake.segemnts[0].ycor() > 280 or snake.segemnts[0].ycor() < -280:
        is_on = False
        scoreboard.game_over()
        
    
    for segment in snake.segemnts[1:]:
        if snake.segemnts[0].distance(segment) < 10:
            is_on = False
            scoreboard.game_over()
            
 
screen.exitonclick()





