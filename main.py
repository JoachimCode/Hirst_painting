from turtle import Turtle, Screen
import colorgram
import random

screen = Screen()
screen.colormode(255)
brush = Turtle()
brush.shapesize(1)
brush.hideturtle()
brush.speed(5 )
amount_of_color = 15
brush.penup()
lines = 10
dots = 10
brush.setpos(-500, -500)


color_pallet = colorgram.extract('painting2.jpeg', amount_of_color)


def define_color(index):
    color = color_pallet[index]
    rgb = color.rgb
    tuplet = (rgb[0], rgb[1], rgb[2])
    return tuplet

list_color = []

for amount in range(amount_of_color):
    list_color.append(define_color(amount))


def draw_dot():
    brush.color(random.choice(list_color))
    brush.dot(20)
    brush.forward(100)

for _ in range(int(lines/2)):
    for _ in range(dots):
        draw_dot()
    brush.back(100)
    brush.left(90)
    brush.forward(100)
    brush.left(90)
    for _ in range(dots):
        draw_dot()
    brush.back(100)
    brush.right(90)
    brush.forward(100)
    brush.right(90)

screen.exitonclick()