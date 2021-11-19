import turtle
from tkinter import messagebox
import pandas as pd

screen = turtle.Screen()
screen.title("Indian States")
screen.setup(height=800, width=800)
image = "IndianStates.gif"
screen.addshape(image)
turtle.shape(image)

gameon = True
state_data = pd.read_csv('indian_states.csv')
state_list = state_data.state_name.tolist()
user_guess = []
correct = 0
chance = 60

while chance != 0:
    indian_state = screen.textinput(title=f"Guess the State {correct}-{36}\n remaining chance {chance}", prompt="Enter the State Name").title()
    if indian_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        ans_state = state_data[state_data.state_name == indian_state]
        x, y = ans_state.x, ans_state.y
        t.goto(int(x), int(y))
        t.write(indian_state)
        state_list.remove(indian_state)
        user_guess.append(indian_state)
        correct += 1
        chance -= 1
    elif indian_state == "Exit":
        break
missing_state = pd.DataFrame(state_list)
missing_state.to_csv("MissingState.csv")
messagebox.showinfo("Result", f"Score is {correct}")
# t.write(}")
screen.exitonclick()

# # Mouse click coordinate selection
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
