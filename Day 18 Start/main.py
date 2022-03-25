import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("deepskyblue")
# tim.forward(100)
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

# for _ in range(20):
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)
#     tim.pd()

import random

# colors = ["steelblue", "crimson", "mediumorchid", "darkorange", "mediumvioletred", "lawngreen", "darkcyan"]


# def draw_shape(num_sides):
#     angel = 360 / num_sides
#     for _ in range(num_sides):
#         tim.right(angel)
#         tim.forward(100)
#
#
# for shape_side_n in range(3, 11):
#     tim.pencolor(random.choice(colors))
#     draw_shape(shape_side_n)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_tuple = (r, g, b)
    return random_tuple


direction = [0, 90, 180, 270]
tim.speed(0)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
# for _ in range(500):
#     tim.pencolor(random_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(50)

screen = t.Screen()
screen.exitonclick()

