from turtle import Turtle

MOVE_DISTANCE = 10 

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POINTS = ((-40, 0), (-20, 0), (0, 0))


class Snake:
    def __init__(self):
        self.x = 0
        self.segemnts = []
        self.create_sanke()
        
        
    def create_sanke(self):
        for position in STARTING_POINTS:
           self.add_segemnet(position)
            
    def add_segemnet(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segemnts.append(tim)
        
    def extend(self):
        self.add_segemnet(self.segemnts[-1].position())
        
         
            
    def move(self):
        for seg_num in range(len(self.segemnts) - 1, 0, -1):
            new_x = self.segemnts[seg_num - 1].xcor()
            new_y = self.segemnts[seg_num - 1].ycor()
            self.segemnts[seg_num].goto(new_x, new_y)
        
        self.segemnts[0].forward(MOVE_DISTANCE)
        
        
    
    def up(self):
        if self.segemnts[0].heading() != DOWN:
            self.segemnts[0].setheading(UP)
             
    def down(self):
        if self.segemnts[0].heading() != UP:
            self.segemnts[0].setheading(DOWN)
        
    def left(self):
        if self.segemnts[0].heading() != RIGHT:
            self.segemnts[0].setheading(LEFT)
        
    def right(self):
        if self.segemnts[0].heading() != LEFT:
            self.segemnts[0].setheading(RIGHT)
        