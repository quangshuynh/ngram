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
    size: int
    R: str
    G: str
    B: str


def move_ball(start_can, end_can):
    if s.empty_stack(start_can):
        raise IndexError("Popped on empty stack")
    else:
        top_of_can = s.top(start_can)
        s.pop(start_can)
        s.push(end_can, top_of_can)


def main():
    initial_red_can = input("Enter the initial configuration in the 'red' can: ")
    green_can = []
    blue_can = []
    bsa.animate_init(initial_red_can)
    moves_required = move_ball(initial_red_can, end_can)
    print("Puzzle solved in " + moves_required + "!")
    input("Close the window to quit.")
    bsa.animate_finish()


if __name__ == "__main__":  # Main guard
    main()
