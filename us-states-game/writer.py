from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, x, y, state):
        self.goto(x, y)
        self.write(state, align="left", font=("Arial", 8, "normal"))

    def missed_state_writer(self, x, y, state):
        self.goto(x, y)
        self.pencolor("red")
        self.write(state, align="left", font=("Arial", 8, "normal"))
