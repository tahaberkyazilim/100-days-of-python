from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#All of the random cars & moving them randomly
#Create cars that are 20px high by 40px wide 
# that are randomly generated along the
#  y-axis and move to the left edge of the
#  screen. No cars should be generated in the
#  top and bottom 50px of the screen 
# (think of it as a safe zone for
#  our little turtle). Hint: generate a new car 
# only every 6th time the game loop runs.
#  If you get stuck, check the video 
# walkthrough in Step 4.

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_maker(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.goto(320, random.randint(-250, 250))
        self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            cur_x = car.xcor()
            new_x = cur_x - self.car_speed
            car.setx(new_x)

    def level_up(self):
            self.car_speed += MOVE_INCREMENT
