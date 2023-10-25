"""
Contains utility functions for working with locations and files.
file: tools.py
language: python3
author: Quang Huynh
"""
def calculate(locations, best_location):
    """
    Calculates the sum of each distance to optimal location
    :param locations: Number of locations
    :param best_location: Optimal location index
    :return: Sum of distances to optimal location
    """
    try:
        sum = 0
        for i in range(len(locations)):
            distance = abs(locations[i] - best_location)
            sum += distance
        return sum
    except TypeError as e:
        print("", end="")


def read(files):
    """
    Opens and reads a text file, extracts, split after a space,
    appends only the numbers in the second half of each line,
    into a list.
    :param: Path to file to be read
    :return: A list of extracted numbers from a file
    """
    numbers = []
    try:
        with open(files, "r") as buildings:
            for line in buildings:
                x = line.split(" ")
                numbers.append(int(x[1]))
            return numbers
    except FileNotFoundError as e:
        print(str(e) + " not found!")





