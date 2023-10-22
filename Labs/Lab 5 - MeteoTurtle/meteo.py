"""
    meteo.py
    assignment: lab 5
    language: python3
    author: Quang Huynh
"""

import turtle as t

def background():
    """
    load the background for the meteo weather map and
    set up the turtle window size and position in the screen's upper left.
    """
    screen = t.Screen()
    screen.bgpic("simland.png")
    t.setup(1100, 650, 0, 0)
    

def draw_rectangle(length, width):
    """
    draws a rectangle with the given length and width
    :param length: length of rectangle
    :param width: width of rectangle
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    t.down()
    for i in range(2):  # Loops 2 L-shaped objects to make a rectangle
        t.fd(length)
        t.left(90)
        t.fd(width)
        t.left(90)


def snowflake(length=8):
    """
    draws a 6-arms snowflake
    :param length: length of line in snowflake
    :pre-conditions: turtle faces east, pen up, color is black
    :post-conditions: turtle faces east, pen up, color is black
    """
    t.down()
    t.color("blue")
    t.begin_fill()
    for i in range(6):  # Loops drawing 6 lines that comes from the center of snowflake
        t.fd(length)
        t.back(length)
        t.left(60)
    t.end_fill()
    t.color("black")

def draw_sun(r=16):
    """
    draws the sun as a circle with a radius of 16
    :param r: the radius of the circle is 16
    :pre-conditions: turtle faces east, pen up, color is black
    :post-conditions: turtle faces east, pen up, color is black
    """
    t.down()
    t.color("yellow")
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.color("black")

def draw_cloudy_sun(size=16):
    """
    draws the sun with a cloud next to it
    :param size: radius for sun and draw_cloud is 16
    :pre-conditions: turtle faces east, pen up, color is black
    :post-conditions: turtle faces east, pen up, color is black
    """
    draw_sun(size)
    t.up()
    t.fd(10)
    t.setheading(270)
    t.fd(10)
    t.setheading(0)
    draw_cloud(size)


def draw_rain(size=16):
    """
    draws the sun as a circle with a radius of 16
    :param size: the length of a rain strip
    :pre-conditions: turtle faces east, pen up, color is black
    :post-conditions: turtle faces east, pen up, color is black
    """
    t.down()
    draw_cloud(size)
    t.color("blue")
    t.up()
    t.back(2 * size)
    t.setheading(270)
    t.fd(10)
    t.setheading(0)
    t.back(4)
    t.setheading(240)
    t.pensize(2)
    for i in range(5):  # Loops drawing rain particles below cloud
        t.fd(size)
        t.up()
        t.back(size)
        t.setheading(0)
        t.fd(10)
        t.setheading(240)
        t.down()
    t.setheading(0)
    t.color("black")


def draw_cloud(r=16):
    """
    draws a pretty cloud as a combination of: 1 circle of radius r,
    2 circles of radius r/2 and a rectangle 2r x r
    :param r:  Radius of circles in cloud
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up, color black
    """
    t.down()
    t.color("blue")
    t.begin_fill()
    t.circle(r/2)
    draw_rectangle(2.2*r, r)
    t.forward(1.2*r)
    t.circle(r)
    t.forward(1.2*r)
    t.circle(r/2)
    t.end_fill()
    t.color("black")
    

def draw_snow(size=8):
    """
    draws 3 snowflakes and a cloud
    :param size: length in pixels
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    draw_cloud(16)
    t.up()
    t.backward(3.75 * size)
    t.right(90)
    t.forward(size)
    t.left(90)
    snowflake(size)
    t.right(45)
    t.forward(2 * size)
    t.left(45)
    snowflake(size)
    t.left(45)
    t.forward(2 * size)
    t.right(45)
    snowflake(size)

def temperature(temp):
    """
    draws a white rectangle with text inside to display temperature
    :param temp: displayed temperature
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    FONT = ("Arial", 9, "bold")  # Font is Arial, Font size is 9, Font type is Bolded
    t.color("white")
    t.begin_fill()
    draw_rectangle(36, 16)
    t.end_fill()
    t.color("black")
    t.up()
    t.fd(8)
    t.write(str(temp) + " F", font=FONT)  # Writes a given temperature in provided font settings
    t.down()


def weather_alert(alert_r):
    """
    draws a red circle to indicate weather alert
    :param alert_r: radius of circle
    :pre-conditions: turtle faces east, pen up, color is black
    :post-conditions: turtle faces east, pen up, color is black
    """
    t.color("red")
    t.circle(alert_r)
    t.color("black")


if __name__ == "__main__":
    background()


