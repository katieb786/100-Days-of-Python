import turtle
import pandas
import writer

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = writer.Writer()


states = pandas.read_csv("50_states.csv")
score = 0
correct_guesses = []

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    state_info = states[states.state == answer_state]
    if answer_state == "Exit":
        break
    if state_info.empty:
        continue
    if answer_state in correct_guesses:
        continue
    writer.write_state(state=answer_state, x=int(state_info.x), y=int(state_info.y))
    correct_guesses.append(answer_state)
    score += 1
    continue

differences = [state for state in states.state if state not in correct_guesses]
# for state in states.state:
#     if state not in correct_guesses:
#         differences.append(state)

missed_states = {
    "state": differences
}

d_states = pandas.DataFrame(missed_states)
d_states.to_csv("missing_states.csv")

for s in d_states.state:
    writer.missed_state_writer(state=s, x=int(states[states.state == s].x), y=int(states[states.state == s].y))

turtle.mainloop()
