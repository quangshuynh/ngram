"""
Program that sorts colored balls into their corresponding cans and animates it
file: ball_puzzle.py
language: python3
author: Quang Huynh
"""

import ball_puzzle_animate as bpa
import cs_stack as s
from dataclasses import dataclass


@dataclass
class Cans:
    red: list
    green: list
    blue: list


def move_ball(stack_list, stack1, stack2):
    """
    Moves ball from one can to another can from a stack list
    :param stack_list: A list of stacks of the colored cans
    :param stack1: Ball from initial can
    :param stack2: Ball to be moved to destination can
    """
    top_of_can = s.pop(stack_list[stack1])
    s.push(stack_list[stack2], top_of_can)
    bpa.animate_move(stack_list, stack1, stack2)


def algorithm(stack_list):
    """
    Sorts all the colored balls into their corresponding colored can
    :param stack_list: A list of stacks of the colored cans
    :return: The number of moves to solve the puzzle
    """
    moves = 0
    while not s.is_empty(stack_list[0]):  # When red can is not empty
        if s.top(stack_list[0]) == "G":   # If top ball is green
            move_ball(stack_list, 0, 1)  # Move to green can
            moves += 1
        else:
            move_ball(stack_list, 0, 2)  # All other colors move from red can to blue can
            moves += 1
    while not s.is_empty(stack_list[2]):  # When blue can is not empty
        if s.top(stack_list[2]) == "R":  # If top ball is red
            move_ball(stack_list, 2, 0)  # Move from blue can to red can
            moves += 1
        else:
            move_ball(stack_list, 2, 1)  # All other colors move from blue can to green can
            moves += 1
    while s.top(stack_list[1]) != "G":  # When top ball is not green
        move_ball(stack_list, 1, 2)  # Move from green can to blue can
        moves += 1
    return moves


def main():
    """
    Initializes the colored cans, solves the ball puzzle, and
    displays how many moves it took to solve the ball puzzle.
    """
    initial_can = input("Enter initial string (R, G, B) of balls in first can: ")  # User inputs colored balls
    bpa.animate_init(initial_can)
    red_can = s.make_empty_stack()  # Red can stack
    green_can = s.make_empty_stack()  # Green can stack
    blue_can = s.make_empty_stack()  # Blue can stack
    colored_cans = [red_can, green_can, blue_can]  # Colored can stack list
    for ball in initial_can:
        s.push(colored_cans[0], ball)  # Pushes the inputted string into the red can
    number_of_moves = algorithm(colored_cans)
    print("Puzzle solved in " + str(number_of_moves) + " moves!")
    print("Close the window to quit")
    bpa.animate_finish()


if __name__ == "__main__":
    main()
