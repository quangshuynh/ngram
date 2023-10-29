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
    return Item(name, int(weight))

def make_box(id,size):
    items = []
    return Box(items, int(size), int(id), int(size))


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
        box_count = 1
        for i in range(len(x)):
            boxes.append(make_box(box_count, x[i]))
            box_count += 1
        for line in file:
            y = line.split(" ")
            items.append(make_item(y[0], y[1]))
        return items, boxes


def insertion_sort_greedy(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j - 1].weight < items[j].weight:
            items[j], items[j - 1] = items[j - 1], items[j]  # Swap
            j -= 1


def greedy1(items, boxes):
    """
    Greedy 1 strategy: Sorts items by decreasing weight and iterate items
    from greatest to lowest weight. Then place item in the box with the biggest
    capacity remaining
    :param items: Items list
    :param boxes: Boxes list
    """
    insertion_sort_greedy(items)  # Implement insertion sort for items list
    for item in items:  # Iterate through sorted items list
        box_greedy1 = 0
        greatest_capacity = 0
        for box in boxes:  # Iterate through boxes
            if box.capacity > greatest_capacity:  # Compare box capacity with the greatest capacity
                box_greedy1 = box
                greatest_capacity = box.capacity
        if item.weight > box_greedy1.capacity:  # If weight of item is bigger than capacity, ignore
            pass
        else:
            box_greedy1.items.append(item)  # Append item if it meets requirements
            box_greedy1.capacity -= item.weight  # Subtract item weight from box capacity
    return (items, boxes)  # Returns a tuple

def greedy2(items, boxes):
    """
    Greedy 2 strategy: Sorts items by decreasing weight and iterate items
    from greatest to lowest weight. Then place item in the box with the lowest
    capacity remaining
    :param items: Items list
    :param boxes: Boxes list
    """
    insertion_sort_greedy(items)  # Implement insertion sort for items list
    for item in items:  # Iterate through sorted items list
        box_greedy2 = 0
        lowest_capacity = 1000
        for box in boxes:  # Iterate through boxes
            # if item doesn't fit in box, check for the next box that fits, check again or: run normal insertion
            # sort, loop through box list, compare item weight and box capacity, if it fits put it in box
            if item.weight < box.size:
                break
            if box.capacity < lowest_capacity:  # Compare box capacity with the greatest capacity
                box_greedy2 = box
                lowest_capacity = box.capacity
        if item.weight > box_greedy2.capacity:  # If weight of item is bigger than capacity, ignore
            pass
        else:
            box_greedy2.items.append(item)  # Append item if it meets requirements
            box_greedy2.capacity -= item.weight  # Subtract item weight from box capacity
    return (items, boxes)  # Returns a tuple


def greedy3(items, boxes):
    """
    Greedy 3 strategy: Sorts items by decreasing weight and iterate through all
    items. Then place items in one box at a time. When the box is full, then
    move onto the next box and place items in that box.
    :param items: Items list
    :param boxes: Boxes list
    """
    insertion_sort_greedy(items)  # Implement insertion sort for items list
    for box in boxes:  # Iterate through sorted boxes list
        box_greedy3 = 0
        for item in items:  # Iterate through items
            current_capacity = 0
            if Box.capacity == current_capacity:  # Compare box capacity with the current capacity
                box_greedy3 = box
        if item.weight > box_greedy3.capacity:  # If weight of item is greater than capacity, ignore
            pass
        else:
            Box.items.append(item)  # Append item if it meets requirements
            box_greedy3.capacity -= items.weight  # Subtract item weight from box capacity
            items.remove(item)  # Remove item from items list
    return (items, boxes)  # Returns a tuple


def output(items, boxes):
    boxed_items = []
    for box in boxes:
        for items_boxed in box.items:
            boxed_items.append(items_boxed)

    if len(items) > len(boxed_items):
        print("Unable to pack all items!")
    else:
        print("All items successfully packed into boxes!")
    for box in boxes:
        print("Box " + str(box.id) + " of weight capacity " + str(box.size) + " contains:")
        for items_box in box.items:
            print(items_box.name + " of weight " + str(items_box.weight))
    boxed_items = []
    for box in boxes:
        for items_boxed in box.items:
            boxed_items.append(items_boxed)

    for item in items:
        if item not in boxed_items:
            print(item.name + " of weight " + str(item.weight) + " got left behind.")

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

    items1 = items
    items2 = items
    items3 = items

    # Apply the three greedy strategies
    greedy1(items1, boxes1)
    greedy2(items2, boxes2)


    # Output
    print("Enter datafile name: " + user_input)
    print("")
    print("Results from Greedy Strategy 1")
    output(items1, boxes1)
    print("")
    print("Results from Greedy Strategy 2")
    output(items2, boxes2)
    #
    # print("Results from Greedy Strategy 3")
    # output(items3, boxes3)


# Main guard
if __name__ == "__main__":
    main()
