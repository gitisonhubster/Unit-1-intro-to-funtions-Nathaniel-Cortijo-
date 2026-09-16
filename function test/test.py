#defining a function 
""" def add(x,y):
    return x + y


print(add(5,15))
z = add(5,15)
print(z) """

import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

def add(x,y):
    return x + y


def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90)

def triangle(x,y):
    for i in range(6):
        t.forward(x)
        t.left(y)
triangle(100,120)



turtle.done