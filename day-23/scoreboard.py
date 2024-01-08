from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 280)
        self.write(f"Level {self.level}")
        
        
    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}")
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over")
        
        
        
        
    
