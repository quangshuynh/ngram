"""
Draw snake-like figures in randomly color fashion, based on a number of segments
file: meteo_turtle.py
language: python3
author: Quang Huynh
"""

import turtle  # imports turtle library
import random  # import random library


# Constants
MAX_SEGMENTS = 500  # Maximum number of segments for a snake
X_BOUNDING_BOX = 80  # X coordinate boundary for snake (from 0, 0)
Y_BOUNDING_BOX = 80  # Y coordinate boundary for snake (from 0, 0)
MIN_LENGTH = 1  # Minimum length for a segment of a snake
MAX_LENGTH = 20  # Maximum length for a segment of snake
MIN_THICKNESS = 1  # Minimum thickness for a segment of snake
MAX_THICKNESS = 10  # Maximum thickness for a segment of snake
MAX_ANGLE = 30  # Maximum turning angle for segment of snake

def draw_snake(segments):
    """
    Draws the recursive snake function using python turtle
    :param segments: Number of segments
    :precondition: Turtle is facing east, turtle pen is up, turtle color is black
    :postcondition: Turtle is facing a random angle, turtle pen is down, turtle color is black
    """
    length = random.randint(MIN_LENGTH, MAX_LENGTH)  # randomly chooses from 1px to 20px
    reverse = 20  # goes back 20 px
    turtle.down()
    if segments == 0:
        return 0
    else:
        turtle.pensize(random.randint(MIN_THICKNESS, MAX_THICKNESS))
        turtle.color(random.random(), random.random(), random.random())
        if -X_BOUNDING_BOX <= turtle.xcor() <= X_BOUNDING_BOX and -Y_BOUNDING_BOX <= turtle.ycor() <= Y_BOUNDING_BOX:
            turtle.fd(length)
        else:
            turtle.right(180)
            turtle.fd(reverse)
        turtle.left(random.randint(-MAX_ANGLE, MAX_ANGLE))
        length -= 1
        return length + draw_snake(segments - 1)


def draw_snake_tail(segments, total_length=0):
    """
    Draws the recursive tail snake function using python turtle
    :param segments: Number of segments
    :param total_length: Total length of the snake drawing
    :precondition: Turtle is facing east, turtle pen is up, turtle color is black
    :postcondition: Turtle is facing a random angle, turtle pen is down, turtle color is black
    """
    length = random.randint(MIN_LENGTH, MAX_LENGTH)  # randomly chooses from 1px to 20px
    reverse = 20  # goes back 20 px
    turtle.down()
    if segments == 0:
        return total_length
    else:
        turtle.color(random.random(), random.random(), random.random())
        turtle.pensize(random.randint(MIN_THICKNESS, MAX_THICKNESS))
        if -X_BOUNDING_BOX <= turtle.xcor() <= X_BOUNDING_BOX and -Y_BOUNDING_BOX <= turtle.ycor() <= Y_BOUNDING_BOX:
            turtle.fd(length)
        else:
            turtle.right(180)
            turtle.fd(reverse)
        turtle.left(random.randint(-MAX_ANGLE, MAX_ANGLE))
        total_length = total_length + length
        return draw_snake_tail(segments - 1, total_length)

def draw_snake_iter(segments):
    """
    Draws the iterative snake function using python turtle
    :param segments: Number of segments
    :precondition: Turtle is facing east, turtle pen is up, turtle color is black
    :postcondition: Turtle is facing a random angle, turtle pen is down, turtle color is black
    """
    reverse = 20  # goes back 20 px
    total = 0
    turtle.down()
    while segments >= 0:
        length = random.randint(MIN_LENGTH, MAX_LENGTH)  # randomly chooses from 1px to 20px
        turtle.pensize(random.randint(MIN_THICKNESS, MAX_THICKNESS))
        turtle.color(random.random(), random.random(), random.random())
        if -X_BOUNDING_BOX <= turtle.xcor() <= X_BOUNDING_BOX and -Y_BOUNDING_BOX <= turtle.ycor() <= Y_BOUNDING_BOX:
            turtle.fd(length)
        else:
            turtle.right(180)
            turtle.fd(reverse)
        turtle.left(random.randint(-MAX_ANGLE, MAX_ANGLE))
        total += length
        segments -= 1
    return total + reverse


def reset():
    """
    Resets the turtle canvas and hides the turtle
    :precondition: Turtle is facing a random angle, turtle pen is down, turtle color is black
    :postcondition: Turtle is facing east, turtle pen is up, turtle color is black
    """
    turtle.reset()
    turtle.hideturtle()


def bounding_box():
    """
    Sets turtle canvas size and world coordinates and draws the bounding box
    :precondition: Turtle is facing east, turtle pen is up, turtle color is black
    :postcondition: Turtle's state is the same as the start of the function
    """
    turtle.setup(600, 600)
    turtle.setworldcoordinates(-150, -150, 150, 150)
    turtle.tracer(0)
    turtle.up()
    turtle.pensize(1)
    turtle.color("black")
    turtle.back(100)
    turtle.setheading(270)
    turtle.forward(100)
    turtle.setheading(0)
    turtle.down()
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)
    turtle.up()
    turtle.goto(0, 0)
    turtle.update()
    turtle.tracer(1)


def main():
    """
    The program creates a picture canvas, draws the bounding box, hides the turtle,
    adjusts turtle speed, asks user for number of segments and draws the snake recursion
    """
    bounding_box()
    turtle.hideturtle()
    turtle.speed(0)
    segments = int(input("Number of segments (0-500): "))
    if MAX_SEGMENTS >= segments >= 0:
        print("Recursive snake’s length is", draw_snake(segments), "units")
        input("Hit enter to continue...")
        reset()
        bounding_box()
        print("Tail recursive snake’s length is", draw_snake_tail(segments, total_length=0), "units")
        input("Hit enter to continue...")
        reset()
        bounding_box()
        print("Iterative snake’s length is", draw_snake_iter(segments), "units")
        print("Close canvas window to end program.")
    else:
        print("Segments must be between 0 and 500 inclusive.")
    turtle.done()


# Main guard
if __name__ == "__main__":
    main()

