"""
Draws a bowtie recursion
file: bowties.py
language: python3
author: Quang Huynh
"""

# Imports turtle
import turtle as t


def draw_one_bowtie(size):
    """
    Draws one bowtie with a circle in the middle
    :param size: The side length of a triangle in a bowtie
    :precondition: Turtle is facing east, turtle pen is up, turtle color is black
    :postcondition: Turtle's state is the same as at start of the function.
    """
    t.pensize(1)
    t.color("blue")
    t.left(30)
    t.down()
    t.fd(size)
    t.right(120)
    t.fd(size)
    t.right(120)
    t.fd(2 * size)
    t.left(120)
    t.fd(size)
    t.left(120)
    t.fd(size)
    t.right(120)
    t.up()
    t.fd(size / 4)
    t.left(90)
    t.color('blue', 'red')
    t.begin_fill()
    t.down()
    t.circle(size / 4)
    t.end_fill()
    t.up()
    t.left(90)
    t.fd(size / 4)
    t.right(90)
    t.color("black")


def draw_bowties(size, depth):
    """
    Recursive function to draw bowties at different depths
    :param size: The side length of a triangle in a bowtie
    :param depth: The depth of recursion
    :preconditions: Turtle is facing east, turtle pen is up, turtle color is black
    :postconditions: Turtle's state is the same as the start of the function
    """
    if depth == 0:  # Base case
        return
    elif depth == 1:
        return draw_one_bowtie(size)
    else: # Recursive case
        draw_one_bowtie(size)
        # Draw four smaller bowties around one bigger bowtie
        t.left(30)
        t.fd(size * 2)
        draw_bowties(size / 3, depth - 1)  # Bowties get smaller by 1/3 and depth decreases by 1
        t.up()
        t.back(size * 2)
        t.right(60)
        t.fd(size * 2)
        t.down()
        draw_bowties(size / 3, depth - 1)
        t.up()
        t.back(size * 2)
        t.right(120)
        t.fd(size * 2)
        t.down()
        draw_bowties(size / 3, depth - 1)
        t.up()
        t.back(size * 2)
        t.right(60)
        t.fd(size * 2)
        t.down()
        draw_bowties(size / 3, depth - 1)
        t.up()
        t.back(size * 2)
        t.right(150)
        return


def main():
    """
    The program creates a picture canvas, resizes the canvas, adjusts
    turtle speed, asks user for number of depths, and draws the bowtie
    recursion
    """
    t.setup(600, 600)  # Turtle canvas size (Square)
    t.speed(10)  # Turtle speed
    depth = int(input("Enter depth: "))
    size = 100  # Maximum bowtie size that is 1/6 of canvas size
    draw_bowties(size, depth)
    t.done()


# Main guard
if __name__ == "__main__":
    main()


