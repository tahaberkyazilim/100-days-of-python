import turtle
import pandas

# Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Writer
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")
state_data = data["state"].tolist()

guessed = []


game = True
while(game):
    state_name = screen.textinput(title = f"{len(guessed)}/{len(state_data)} States Correct", prompt =  "Enter a state name: ")
    if state_name is None:
            game = False
            break
    state_name = state_name.title()
    if state_name in state_data:
            loc_x = data[data["state"] == state_name]["x"].item()
            loc_y = data[data["state"] == state_name]["y"].item()
            if state_name not in guessed:
                            guessed.append(state_name)
                            writer.goto(loc_x, loc_y)
                            writer.write(state_name)
            if len(guessed) == len(state_data):
                    game = False
                 
    else:
        print("Wrong!")

states_to_learn = []

for state in state_data:
        if state not in guessed:
                states_to_learn.append(state)


new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")


screen.exitonclick()

