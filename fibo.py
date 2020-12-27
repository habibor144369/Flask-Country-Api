# Draw the Fibonacci Spiral using Turtle Graphics

from turtle import *
import turtle
turtle.pensize(2)
turtle.color("green")

fib_nr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]  # Fibonacci numbers this could be calculated instead


def draw_square(side_length):  # Function for drawing a square
    for i in range(4):
        forward(side_length)
        right(90)


nr_squares = len(fib_nr)

factor = 6  # Enlargement factor
penup()
goto(50, 50)  # Move starting point right and up
pendown()
for i in range(nr_squares):
    draw_square(factor * fib_nr[i])  # Draw square
    penup()  # Move to new corner as starting point
    forward(factor * fib_nr[i])
    right(90)
    forward(factor * fib_nr[i])
    pendown()

penup()
goto(50, 50)  # Move to starting point
setheading(0)  # Face the turtle to the right
pencolor('red')
pensize(2)
pendown()

# Draw quarter circles with fibonacci numbers as radius
for i in range(nr_squares):
    circle(-factor * fib_nr[i], 90)  # minus sign to draw clockwise

turtle.hideturtle()
turtle.done()
print("# Thank You Allah For Help Me!") # Thank You Allah For Help Me!