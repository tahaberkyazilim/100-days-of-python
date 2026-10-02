from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#The turtle that crossing the street


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self, MOVE_DISTANCE):
        cur_y = self.ycor()
        new_y = cur_y + MOVE_DISTANCE
        self.sety(new_y)

    def go(self):
        self.move(MOVE_DISTANCE)   

    def is_at_finish_line(self):
            if self.ycor() >= FINISH_LINE_Y:
                return True
            else:
                 return False
    
    def refresh(self):
        self.goto(STARTING_POSITION)

    
            

    
