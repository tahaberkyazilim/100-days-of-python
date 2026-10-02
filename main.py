import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#In the upcoming lessons, we have created step-by-step instructions to help you complete this project.

#Difficulty Normal 😎: Use all Steps to complete the project.

#Difficulty Hard 🤔: Use only Steps 1 and 2 to complete the project.

#Difficulty Expert 🤯: Only use Step 1 to complete the project.


#For all difficulty levels, begin by downloading the turtle
# -crossing-start.zip from this lesson's resources and opening it in PyCharm.
#  The starting project contains the starting code for the game, we'll walk through
#  the code in the starting project in the next lesson.

#Alternatively, you can create the entire project from scratch by 
# creating a blank project inside PyCharm and create a Turtle screen that is 600px
#  by 600px. You'll also need to turn off tracer(0) and use update() to refresh the screen
#  every 0.1s. If you are confused about this, just use the starting project instead.

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go, "Up")

game_is_on = True
counter = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.update()
    if counter % 6 == 0:
        cars.car_maker()
    cars.move()
    counter += 1

    #Detecting the collision 
    for car in cars.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

    #Speeding up
    if player.is_at_finish_line():
        player.refresh()
        cars.level_up()
        score.increase_score()




screen.exitonclick()
