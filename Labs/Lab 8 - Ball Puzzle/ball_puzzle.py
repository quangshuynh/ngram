"""
Program that sorts colored balls into their corresponding cans
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


colored_cans = [s.make_empty_stack(), s.make_empty_stack(), s.make_empty_stack()]  # Red, green, blue


def move_ball(start_can, end_can, stack_list):
    if not s.is_empty(stack_list[0]):
        top_of_can = s.top(stack_list[0])
        if top_of_can == "R":
            s.pop(stack_list[0])
            s.push(stack_list[1], top_of_can)
            bsa.animate_move(stack_list, 0, 1)
        if top_of_can == "G":
            s.pop(stack_list[0])
            s.push(stack_list[1], top_of_can)
            bsa.animate_move(stack_list, 0, 1)
        if top_of_can == "B":
            s.pop(stack_list[0])
            s.push(stack_list[1], top_of_can)
            bsa.animate_move(stack_list, 0, 2)


def algorithm(initial_can, stack_list):
    moves = 0
    while not s.is_empty(stack_list[0]) or not s.is_empty(stack_list[1]) or not s.is_empty(stack_list[2]):
        top_of_can = s.top(stack_list[0])
        if top_of_can == "R":
            if s.is_empty(stack_list[1]):
                move_ball(stack_list[0], stack_list[2], stack_list)
            elif s.is_empty(stack_list[2]):
                move_ball(stack_list[0], stack_list[1], stack_list)
            else:
                move_ball(stack_list[0], stack_list[1], stack_list)
        elif top_of_can == "G":
            if s.is_empty(stack_list[0]):
                move_ball(stack_list[1], stack_list[2], stack_list)
            elif s.is_empty(stack_list[2]):
                move_ball(stack_list[1], stack_list[0], stack_list)
            else:
                move_ball(stack_list[1], stack_list[2], stack_list)
        elif top_of_can == "B":
            if s.is_empty(stack_list[0]):
                move_ball(stack_list[2], stack_list[1], stack_list)
            elif s.is_empty(stack_list[1]):
                move_ball(stack_list[2], stack_list[0], stack_list)
            else:
                move_ball(stack_list[2], stack_list[1], stack_list)
        moves += 1
    return moves


def main():
    initial_can = input("Enter the configuration in the initial can: ")
    for ball in initial_can:
        s.push(colored_cans[0], ball)
    bsa.animate_init(initial_can)
    number_of_moves = algorithm(initial_can, colored_cans)
    print("Puzzle solved in " + str(number_of_moves) + " moves!")
    input("Close the window to quit.")
    bsa.animate_finish()


if __name__ == "__main__":
    main()
