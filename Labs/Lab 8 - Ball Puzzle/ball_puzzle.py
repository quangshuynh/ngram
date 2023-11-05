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


def initialization():
    """
    Create three empty stacks for each colored can and initialize
    stacks to represent colored cans. Then, asks user input for
    configuration of initial can, pushes each ball from the initial
    can onto the red can stack and animates the initialization.
    :return: A list that has the three colored cans (Red, green, blue)
    """
    red_can = s.make_empty_stack()
    green_can = s.make_empty_stack()
    blue_can = s.make_empty_stack()
    colored_cans = [red_can, green_can, blue_can]
    initial_can = input("Enter the configuration in the initial can: ")
    for ball in initial_can:
        s.push(colored_cans[0], ball)
    bpa.animate_init(initial_can)
    return colored_cans


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
    while not s.is_empty(stack_list[0]):
        if s.top(stack_list[0]) == "G":
            move_ball(stack_list, 0, 1)
            moves += 1
        else:
            move_ball(stack_list, 0, 2)
            moves += 1
    while not s.is_empty(stack_list[2]):
        if s.top(stack_list[2]) == "R":
            move_ball(stack_list, 2, 0)
            moves += 1
        else:
            move_ball(stack_list, 2, 1)
            moves += 1
    while s.top(stack_list[1]) != "G":
        move_ball(stack_list, 1, 2)
        moves += 1
    return moves


def main():
    """
    Initializes the colored cans, solves the puzzle, and
    displays the number of moves it took to solve the puzzle.
    """
    stack_list = initialization()
    number_of_moves = algorithm(stack_list)
    print("Puzzle solved in " + str(number_of_moves) + " moves!")
    print("Close the window to quit")
    bpa.animate_finish()



if __name__ == "__main__":
    main()
