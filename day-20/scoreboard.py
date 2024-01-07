from turtle import  Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(-40, 270)
        self.hideturtle()
        self.write(f"Score: {self.score}", font={"Arial", 6, "normal"})    
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font={"Arial", 6, "normal"})    
        
    def game_over(self):
        self.setposition(-40, 0)
        self.write(f"Game Over", font={"Arial", 6, "normal"})    
        
        
        
        
        

        
        
