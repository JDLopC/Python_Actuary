# import math
import random as rnd
import turtle as t

tim = t.Turtle()

colors = ['pink', 'brown', 'yellow', 'black', 'red', 'blue']

for i in range(3, 11):
    tim.color(rnd.choice(colors))
    for _ in range(i):
        tim.right(360/i)
        tim.forward(100)


screen = t.Screen()
screen.exitonclick()