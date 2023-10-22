"""
Draws scenery in a forest
language: python3
file: scenery.py
author: Quang Huynh
"""

# import turtle, random and math from python library
import math
import random
import turtle

# Sets canvas background color to light blue
turtle.bgcolor("lightblue")

# Canvas setup
turtle.setworldcoordinates(-100, -100, 400, 325)

# Default pixels
total_pixels = 0

"""
Draws a pine tree that has a random trunk size between 50px-200px;
The sides of the triangle on top are equilateral and 60% of the trunk size
:precondition: Turtle is facing east, turtle pen is up, turtle color is black
:postcondition: Turtle's state is the same as at start of the function.
"""
def pine_tree():
    # Randomly chooses a trunk size between 50px and 200px
    p_length = random.randint(50, 200)
    turtle.up()
    turtle.setheading(90)
    turtle.up()
    turtle.fd(p_length)
    turtle.left(90)
    turtle.down()
    turtle.color("green")
    turtle.fd(p_length * 0.3)
    turtle.right(120)
    turtle.fd(p_length * 0.6)
    turtle.right(120)
    turtle.fd(p_length * 0.6)
    turtle.right(120)
    turtle.fd(p_length * 0.3)
    turtle.left(90)
    turtle.fd(p_length)
    turtle.up()
    turtle.setheading(0)
    turtle.color("black")
    return (3 * 0.6 * p_length) + p_length


"""
Draws a house with 100px walls and base;
The roof has a 45 degree angle
:precondition: Turtle is facing east, turtle pen is up, turtle color is black
:postcondition: Turtle's state is the same as at start of the function.
"""
def house(house_position, house_color, total_pixels=0):
    # House variables
    h_length = 100
    h_roof_length = 50 * math.sqrt(2)
    # Code to write positioning (1, 2, 3)
    if house_position == 1:
        # Draws the ground/grass
        total_pixels += ground()
        turtle.up()
        turtle.forward(200)
        turtle.down()
        # Draws tree 1
        total_pixels += random_tree()
        turtle.up()
        turtle.forward(100)
        turtle.down()
        # Draws tree 2
        total_pixels += random_tree()
        turtle.up()
        turtle.back(300)
        turtle.down()
    elif house_position == 2:
        # Draws the ground/grass
        total_pixels += ground()
        # Draws tree 1
        total_pixels += random_tree()
        turtle.up()
        turtle.forward(300)
        turtle.down()
        # Draws tree 2
        total_pixels += random_tree()
        turtle.up()
        turtle.back(200)
        turtle.down()
    elif house_position == 3:
        # Draws the ground/grass
        total_pixels += ground()
        # Draws tree 1
        total_pixels += random_tree()
        turtle.up()
        turtle.forward(100)
        turtle.down()
        # Draws tree 2
        total_pixels += random_tree()
        turtle.up()
        turtle.forward(100)
    turtle.color(house_color)
    turtle.down()
    turtle.setheading(0)
    turtle.fd(h_length)
    turtle.left(90)
    turtle.fd(h_length)
    turtle.left(45)
    turtle.fd(h_roof_length)
    turtle.left(90)
    turtle.fd(h_roof_length)
    turtle.left(45)
    turtle.fd(h_length)
    turtle.up()
    turtle.setheading(0)
    turtle.color("black")
    return (3 * h_length) + (2 * h_roof_length) + total_pixels


"""
Draws a maple tree that has a random trunk size between 50px-150px;
The radius of the circle on top is 40% of the trunk size
:precondition: Turtle is facing east, turtle pen is up, turtle color is black
:postcondition: Turtle's state is the same as at start of the function.
"""
def maple_tree():
    m_length = random.randint(50, 150)
    turtle.up()
    turtle.setheading(90)
    turtle.fd(m_length)
    turtle.setheading(0)
    turtle.color("green")
    turtle.down()
    turtle.circle(m_length * 0.4)
    turtle.setheading(270)
    turtle.fd(m_length)
    turtle.up()
    turtle.setheading(0)
    turtle.color("black")
    return (m_length * 0.4) + m_length


"""
Draws the ground
:precondition: Turtle is facing east, turtle is color is black, turtle pen is up
:postcondition: Turtle's state is the same as at start of the function.
"""
def ground():
    g_length = 500
    turtle.down()
    turtle.color("green")
    turtle.back(100)
    turtle.fd(g_length)
    turtle.up()
    turtle.back(400)
    return g_length


# Draws either a pine tree or maple tree
def random_tree():
    # Generate random tree types
    tree = random.choice(["pine", "maple"])
    if tree == "pine":
        turtle.up()
        turtle.down()
        return pine_tree()
    else:
        turtle.up()
        turtle.down()
        return maple_tree()

# User inputs
def main(total_pixels=0):
    # Ask user if they want to add a house
    house_add = input("Add house to forest? (y, n): ")
    # If user says they want to add a house
    if house_add == "y":
        house_position = int(input("At what position? (1, 2, 3): "))
        house_color = input("What color is the house?: ")
        total_pixels += house(house_position, house_color)
        # Moves the turtle back 100 pixels if in position 2
        if house_position == 2:
            turtle.back(100)
        # Moves the turtle back 200 pixels if in position 2
        elif house_position == 3:
            turtle.back(200)

    # If user says they don't want to add a house (Add tree 3)
    if house_add == "n":
        # Draws the ground/grass
        total_pixels += ground()
        # Draws 3 random trees
        for i in range(3):
            total_pixels += random_tree()
            turtle.forward(100)
        turtle.up()
        turtle.back(300)
    # Amount of ink used
    print("We used " + str(total_pixels) + " units of ink for the drawing")
    print("Close the canvas window to end the program")
    # Blocks until user closes the canvas window.
    turtle.done()


if __name__ == "__main__":
    main()

