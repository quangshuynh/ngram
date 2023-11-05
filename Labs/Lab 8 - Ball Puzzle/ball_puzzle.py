"""
Program that sorts colored balls into their corresponding cans and animates it
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


def in_it():
    # colored_cans = [s.make_empty_stack(), s.make_empty_stack(), s.make_empty_stack()]  # Colored can list: red, green, blue
    stack1 = s.make_empty_stack()
    stack2 = s.make_empty_stack()
    stack3 = s.make_empty_stack()
    colored_cans = [stack1, stack2, stack3]
    initial_can = input("Enter the configuration in the initial can: ")
    for ball in initial_can:
        s.push(colored_cans[0], ball)
    bsa.animate_init(initial_can)
    return colored_cans


def move_ball(stack_list, stack1, stack2):
    top_of_can = s.pop(stack_list[stack1])
    s.push(stack_list[stack2], top_of_can)
    bsa.animate_move(stack_list, stack1, stack2)
    # if not s.is_empty(stack_list[0]):
    #     top_of_can = s.top(stack_list[0])
    #     if top_of_can == "R":
    #         s.pop(stack_list[0])
    #         s.push(stack_list[1], top_of_can)
    #         bsa.animate_move(stack_list, 0, 1)
    #     if top_of_can == "G":
    #         s.pop(stack_list[0])
    #         s.push(stack_list[1], top_of_can)
    #         bsa.animate_move(stack_list, 0, 1)
    #     if top_of_can == "B":
    #         s.pop(stack_list[0])
    #         s.push(stack_list[1], top_of_can)
    #         bsa.animate_move(stack_list, 0, 2)


def algorithm(stack_list):
    moves = 0
    # bsa.animate_move(stack_list, stack_list[0], stack_list[1])
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
    stack_list = in_it()
    number_of_moves = algorithm(stack_list)
    print("Puzzle solved in " + str(number_of_moves) + " moves!")
    input("Close the window to quit.")
    bsa.animate_finish()


if __name__ == "__main__":
    main()
