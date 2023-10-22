"""
Use python turtle graphics to print out two road signs, one of which has to include an intersection sign.
file: signs.py
description: python turtle road signs
language: python3
author: Quang Huynh
"""

# Imports the turtle library, allowing pictures to be drawn on a canvas window
import turtle


# Modifies the canvas size and position of the window
turtle.setworldcoordinates(-450, -400, 450, 400)
turtle.setup(650, 650)


"""
Draws a yellow rhombus with a black outline (Road sign template)
:precondition: Turtle is facing east, turtle is up, turtle color is black
:postcondition: Turtle is facing 315°, turtle is up, turtle color is yellow with black outline
"""
def yellow_rhombus():
    turtle.down()
    turtle.color('black', 'yellow')
    turtle.begin_fill()
    turtle.pensize(2)
    turtle.left(45)
    turtle.fd(100)
    for i in range(4):
        turtle.left(90)
        turtle.fd(100)
    turtle.end_fill()
    turtle.up()


"""
Draws traffic lights symbol
:precondition: Turtle is facing east, turtle is up, turtle color is black
:postcondition: Turtle is on the bottom left edge of traffic light
:postcondition: Turtle is facing east, turtle is up, turtle color is black
"""
def lights():
    turtle.up()
    turtle.back(14)
    turtle.setheading(90)
    turtle.fd(110)
    turtle.setheading(0)
    turtle.down()
    turtle.color('black')
    turtle.begin_fill()
    turtle.forward(30)
    turtle.right(90)
    turtle.fd(80)
    turtle.right(90)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(80)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(0)
    turtle.fd(5)
    turtle.setheading(270)
    turtle.fd(13)
    turtle.color('red')
    turtle.begin_fill()
    turtle.down()
    turtle.circle(10)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(270)
    turtle.fd(25)
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(270)
    turtle.fd(25)
    turtle.color('green')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.back(5)
    turtle.setheading(270)
    turtle.fd(16)
    turtle.setheading(0)
    turtle.color("black")


"""
Draws an intersection symbol
:precondition: Turtle is facing 315, turtle color is black, turtle is up
:postcondition: Turtle is facing 180, turtle color is black, turtle is up
"""
def intersection():
    turtle.up()
    turtle.color('black')
    turtle.setheading(0)
    turtle.back(10)
    turtle.setheading(90)
    turtle.fd(105)
    turtle.setheading(0)
    turtle.begin_fill()
    turtle.down()
    turtle.fd(20)
    turtle.right(90)
    turtle.fd(75)
    turtle.right(90)
    turtle.fd(20)
    turtle.right(90)
    turtle.forward(75)
    turtle.end_fill()
    turtle.up()
    turtle.setheading(0)
    turtle.down()
    turtle.color('black')
    turtle.begin_fill()
    turtle.back(15)
    turtle.setheading(270)
    turtle.fd(15)
    turtle.left(90)
    turtle.forward(36)
    turtle.fd(13)
    turtle.left(90)
    turtle.fd(15)
    turtle.left(90)
    turtle.fd(13)
    turtle.end_fill()
    turtle.up()



# Draws a traffic lights ahead road sign
def traffic_light():
    yellow_rhombus()
    turtle.back(100)
    turtle.setheading(0)
    lights()


# Draws a yellow sign with T for intersection
def intersection_sign():
    yellow_rhombus()
    turtle.back(100)
    turtle.setheading(0)
    intersection()


"""
The program creates a picture canvas, draws an intersection sign,
goes home, draws a traffic light sign, goes home and finishes.
"""
def lab1():
    turtle.home()
    turtle.up()
    turtle.back(170)
    turtle.down()
    intersection_sign()
    turtle.home()
    turtle.back(20)
    traffic_light()
    turtle.color('black', 'black')
    turtle.up()
    turtle.home()
    turtle.done()


# Calling the lab function that draws a T intersection sign and traffic light sign
lab1()
