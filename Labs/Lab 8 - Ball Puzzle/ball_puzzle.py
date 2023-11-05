"""
*add description**
file: ball_puzzle.py
language: python3
author: Quang Huynh
"""


import ball_puzzle_animate as bsa
import cs_stack as s
from dataclasses import dataclass


@dataclass
class Cans:
    red: list
    green: list
    blue: list


red = s.mk_empty_stack()
green = s.mk_empty_stack()
blue = s.mk_empty_stack()

cans = [red, green, blue]


def move_ball(start_can, end_can):
    if s.empty_stack(start_can):
        raise IndexError("Popped on empty stack")
    else:
        top_of_can = s.top(start_can)
        s.pop(start_can)
        s.push(end_can, top_of_can)


def algorithm(initial_can):
    moves = 0

    while red or green or blue:
        top_of_can = s.top(initial_can)
        if top_of_can == "R":
            if not green:
                move_ball("red", "blue")
            elif not blue:
                move_ball("red", "green")
            else:
                move_ball("red", "green")
        elif top_of_can == "G":
            move_ball("green", "red")
        elif top_of_can == "B":
            move_ball("blue", "red")
        moves += 1
    return moves

def main():
    initial_can = input("Enter the initial configuration in the 'red' can: ")
    bsa.animate_init(initial_can)
    number_of_moves = algorithm(initial_can)
    print("Puzzle solved in" + str(number_of_moves) + "!")
    input("Close the window to quit.")
    bsa.animate_finish()


if __name__ == "__main__":  # Main guard
    main()
