import turtle
import pandas


def get_cor():
    new_state = data[data.state == guess]
    state_cor = (int(new_state.x), int(new_state.y))
    return state_cor


def create_turtle(new_cor, state_name):
    tim = turtle.Turtle()
    tim.penup()
    tim.hideturtle()
    tim.goto(new_cor)
    tim.write(f"{state_name}")


data = pandas.read_csv("50_states.csv")
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US Guess State")
screen.addshape(image)
turtle.shape(image)

game_on = True
total_states = len(data.state)
state_list = data.state.to_list()
guessed_states = []

while game_on:
    right_answers = len(guessed_states)
    guess = screen.textinput(title=f"{right_answers}/{total_states}", prompt="What's another state's name").title()

    if guess == "Exit":
        states_to_learn = [state for state in state_list if state not in guessed_states]
        to_learn = pandas.DataFrame(states_to_learn)
        to_learn.to_csv("states_to_learn.csv")
        break

    if guess in state_list:
        cor = get_cor()
        create_turtle(cor, guess)
        guessed_states.append(guess)
    else:
        print("There is no such State")

    if right_answers == total_states:
        print("You Won! Congratulations")
        game_on = False


# Method 1
#
# import turtle
# import pandas
#
#
# def get_cor():
#     state_cor = (int(state.x), int(state.y))
#     return state_cor
#
#
# def create_turtle(new_cor, state_name):
#     tim = turtle.Turtle()
#     tim.penup()
#     tim.hideturtle()
#     tim.goto(new_cor)
#     tim.write(f"{state_name}")
#
#
# def score(current_score):
#     current_score += 1
#     return current_score
#
#
# data = pandas.read_csv("50_states.csv")
# image = "blank_states_img.gif"
# screen = turtle.Screen()
# screen.title("US Guess State")
# screen.addshape(image)
# turtle.shape(image)
#
# game_on = True
# right_answers = 0
# total_states = len(data.state)
#
#
# while game_on:
#     guess = screen.textinput(title=f"{right_answers}/{total_states}", prompt="What's another state's name").title()
#     state = data[data.state == guess]
#     if any(data.state.isin([guess])):
#         cor = get_cor()
#         create_turtle(cor, guess)
#         right_answers = score(right_answers)
#     else:
#         print("There is no such State")
# if right_answers == total_states:
#     print("You Won! Congratulations")
#     game_on = False
#
# screen.mainloop()




# Method 2

# import turtle
# import pandas
#
#
# def get_cor():
#     new_state = data[data.state == guess]
#     state_cor = (int(new_state.x), int(new_state.y))
#     return state_cor
#
#
# def create_turtle(new_cor, state_name):
#     tim = turtle.Turtle()
#     tim.penup()
#     tim.hideturtle()
#     tim.goto(new_cor)
#     tim.write(f"{state_name}")
#
#
# data = pandas.read_csv("50_states.csv")
# image = "blank_states_img.gif"
# screen = turtle.Screen()
# screen.title("US Guess State")
# screen.addshape(image)
# turtle.shape(image)
#
# game_on = True
# total_states = len(data.state)
# state_list = data.state.to_list()
# guessed_states = []
#
# while game_on:
#     right_answers = len(guessed_states)
#     guess = screen.textinput(title=f"{right_answers}/{total_states}", prompt="What's another state's name").title()
#
#     if guess == "Exit":
#         states_to_learn = []
#         for state in state_list:
#             if state not in guessed_states:
#                 states_to_learn.append(state)
#
#         to_learn = pandas.DataFrame(states_to_learn)
#         to_learn.to_csv("states_to_learn.csv")
#         break
#
#     if guess in state_list:
#         cor = get_cor()
#         create_turtle(cor, guess)
#         guessed_states.append(guess)
#     else:
#         print("There is no such State")
#
#     if right_answers == total_states:
#         print("You Won! Congratulations")
#         game_on = False