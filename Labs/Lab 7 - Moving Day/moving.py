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
    return Box(items, int(size), id, int(capacity))


def read(file):
    """
    Read data from a file and sort lists of boxes and items.
    :param file: Input file
    :return: Items list and boxes list
    """
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


def greedy1(items, boxes):
    items.sort(key=lambda x: x.weight, reverse=True)
    for item in items:
        boxes.sort(key=lambda x: x.capacity, reverse=True)
        for box in boxes:
            if item.weight <= box.capacity:
                box.items.append(item)
                box.capacity -= item.weight
                break


def greedy2(items, boxes):
    pass


def greedy3(items, boxes):
    pass


def output(boxes):
    pass


def main():
    """
    pass
    """
    user_input = input("What file do you want to select? ")
    items, boxes = read(user_input)

    # Copy boxes to apply multiple strategies
    boxes1 = [Box([], box.capacity, box.id, box.size) for box in boxes]
    boxes2 = [Box([], box.capacity, box.id, box.size) for box in boxes]
    boxes3 = [Box([], box.capacity, box.id, box.size) for box in boxes]

    # Apply the three greedy strategies
    greedy1(items, boxes1)
    greedy2(items, boxes2)
    greedy3(items, boxes3)

    # Output
    print("Results from Greedy Strategy 1")
    output(boxes1)

    print("Results from Greedy Strategy 2")
    output(boxes2)

    print("Results from Greedy Strategy 3")
    output(boxes3)


# Main guard
if __name__ == "__main__":
    main()
