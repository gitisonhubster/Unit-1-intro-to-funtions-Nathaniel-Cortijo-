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

sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
""" square(100,90) """

def triangle(x,y):
    for i in range(6):
        t.forward(x)
        t.left(y)
""" triangle(100,120) """

def square_sircle (x,y):
    for i in range(60):
       square(x,y)
       t.right(5)
""" square_sircle(100,90) """

def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
""" doubleSquares(5) """

def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
""" addSquares(5) """

def square_spiral (y):
    c = 5
    for i in range(60):
       square(c,y)
       t.left(-5)
       c = add(c,5)
""" square_spiral(90) """

def star(x,y):
   for i in range(5):
        t.forward(x)
        t.left(y)
""" star(100,144) """

def star_spiral (y):
    c = 5
    for i in range(60):
       star(c,y)
       t.left(-5)
       c = add(c,5)
star_spiral(144)

turtle.done