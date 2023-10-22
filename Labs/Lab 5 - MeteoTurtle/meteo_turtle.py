"""
An interpreter that draws weather symbols when a command string is inputted
file: meteo_turtle.py
language: python3
author: Quang Huynh
"""

import turtle  # imports turtle library
import meteo as m  # imports meteo.py


def get_number(string):
    """
    grabs only the numbers from a command string
    :param string: inputted command string
    :return: extracted numbers from string
    """
    str = " "
    for i in range(0, len(string)):  # Loop that goes through 0 to length of a string
        if string[i].isdigit() or string[i] == "-":  # Checks if string has a number or has a negative sign
            str += string[i]  # Adds extracted number/negative sign to x
        else:
            break
    return str


def interpret(string):
    """
    grabs only the letters from a command string
    :param string: inputted command string
    """
    try:
        while string != "":
            if string[0] == "S":
                string = process_s(string)
            elif string[0] == "P":
                string = process_p(string)
            elif string[0] == "C":
                string = process_c(string)
            elif string[0] == "W":
                string = process_w(string)
            elif string[0] == "R":
                string = process_r(string)
            elif string[0] == "T":
                string = process_t(string)
            elif string[0] == "A":
                string = process_a(string)
            elif string[0] == "G":
                string = process_g(string)
            else:
                print("Unrecognized command")
                return None
    except TypeError as error:  # Will return None if error is detected
        print("Unrecognized command")
        return None


# Processes
def process_s(string):
    """
    draws a sun
    :param string: inputted command string after "S"
    return: the remaining string after processing "S".
    """
    try:
        str = string[1:]  # Proceeds after S
        m.draw_sun()
        return str
    except ValueError as error:  # Will return None if error is detected
        print("Error in process_s")
        return None



def process_p(string):
    """
    draws a cloudy sun
    :param string: inputted command string after "P"
    return: the remaining string after processing "P"
    """
    try:
        str = string[1:]  # Proceeds after P
        m.draw_cloudy_sun()
        return str
    except ValueError as error:  # Will return None if error is detected
        print("Error in process_p")
        return None


def process_c(string):
    """
    draws cloud
    :param string: inputted command string after "C"
    return: the remaining string after processing "C"
    """
    try:
        str = string[1:]  # Proceeds after C
        m.draw_cloud()
        return str
    except ValueError as error:  # Will return None if error is detected
        print("Error in process_c")
        return None


def process_w(string):
    """
    draws a cloud with snow falling
    :param string: inputted command string after "W"
    return: the remaining string after processing "W"
    """
    try:
        str = string[1:]  # Proceeds after W
        m.draw_snow()
        return str
    except ValueError as error:  # Will return None if error is detected
        print("Error in process_w")
        return None


def process_r(string):
    """
    draws a cloud with rain falling
    :param string: inputted command string after "R"
    :return: the remaining string after processing "R"
    """
    try:
        str = string[1:]  # Proceeds after R
        m.draw_rain()
        return str
    except ValueError as error:  # Will return None if error is detected
        print("Error in process_r")
        return None


def process_t(string):
    """
    draws white rectangle with temperature value text
    :param string: inputted command string after "T"
    :return: the remaining string after processing "T" and temperature value
    """
    try:
        str = string[1:]  # Proceeds after T
        temp_str = get_number(str)
        str = string[len(temp_str):]  # Proceed after temperature value
        temp = int(temp_str)
        m.temperature(temp)
        return str
    except ValueError as error:  # Will return None if error is detected
        print("Error in process_t")
        return None


def process_a(string):
    """
    draws circle with red outline according to radius
    :param string: inputted command string after "A"
    :return: the remaining string after processing "A" and radius value
    """
    try:
        str = string[1:]  # Proceed after A
        radius_str = get_number(str)
        str = string[len(radius_str):]  # Proceed after radius value
        radius_int = int(radius_str)
        m.weather_alert(radius_int)
        return str
    except ValueError as error:  # Will return None if error is detected
        print("Error in process_a")
        return None


def process_g(string):
    """
    moves turtle to a given coordinate
    :param string: inputted command string after "G"
    :return: the remaining string after processing "G", comma, and coordinates.
    """
    try:
        turtle.up()
        str = string[1:]  # Get rid of "G"
        x_str = get_number(str)  # Grabs x value
        str = str[len(x_str):]  # Proceed after "," and x-coordinate
        y_str = get_number(str)  # Grabs y value
        str = str[len(y_str) - 1:]  # Proceed after y-coordinate
        x = int(x_str)
        y = int(y_str)
        turtle.goto(x, y)
        turtle.down()
        return str
    except ValueError as error:  # Will return None if error is detected
        print("Error in process_g")
        return None


def main():
    """
    program that interprets a command string, draws weather symbols,
    and waits for the user to close the program.
    """
    turtle.hideturtle()
    turtle.speed(0)
    string = input("Enter command string: ")
    m.background()
    interpret(string)
    turtle.done()


# Main guard
if __name__ == "__main__":
    main()

