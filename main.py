import turtle
import random
import colorgram
from turtle import Turtle, Screen
turtle.colormode(255)
colors = colorgram.extract('n.jpg', 45)
c = []
for i in range(0, len(colors)):
    first_color = colors[i]
    a = first_color.rgb
    d = (a[0], a[1], a[2])
    c.append(d)
tim = Turtle()
a = 0.00
b = 0.00
tim.penup()
tim.goto(-200.00, -200.00)
tim.speed("fastest")
for i in range(0, 100):
    if i % 10 == 0:
        a += 50
        tim.goto(-200.00, -200.00 + a)
        tim.dot(20, random.choice(c))
        tim.penup()
        tim.forward(50)
    else:
        tim.dot(20, random.choice(c))
        tim.penup()
        tim.forward(50)





screen = Screen()
screen.exitonclick()
