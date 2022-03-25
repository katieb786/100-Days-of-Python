from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["tim", "tom", "tina", "terri", "travis", "tracy"]
all_turtles = []
y_position = [-100, -60, -20, 20, 60, 100]

for num in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[num])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose. The {winning_color} turtle is the winner!")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


screen.exitonclick()
