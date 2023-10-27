"""
This program defines dataclasses and  functions to create instances of these classes,
read data from a file, and display the resulting boxes and items.
file: moving.py
language: python3
author: Quang Huynh
"""

from dataclasses import dataclass

@dataclass
class Box:
    items: list
    capacity: int
    id: int
    size: int


@dataclass
class Item:
    name: str
    weight: int


def make_item(name, weight):
    return Item(name, weight)

def make_box(id, capacity):
    size = 0
    items = []
    return Box(items, int(size), id, capacity)


def read(file):
    boxes = []
    items = []
    with open(file, "r") as file:
        line = file.readline()
        x = line.split(" ")
        for i in range(len(x)):
            boxes.append(make_box(i, x[i]))
        for line in file:
            y = line.split(" ")
            items.append(make_box(y[0], y[1]))
        return items, boxes


def main():
    user_input = input("What file do you want to select? ")
    items, boxes = read(user_input)
    print(boxes)
    print(items)


# Main guard
if __name__ == "__main__":
    main()