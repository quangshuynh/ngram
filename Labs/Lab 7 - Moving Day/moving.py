"""
This program defines dataclasses and  functions to create instances of these classes,
read data from a file, and display the resulting boxes and items.
file: moving.py
language: python3
author: Quang Huynh
"""

from dataclasses import dataclass

@dataclass  # Box dataclass
class Box:
    items: list
    capacity: int
    id: int
    size: int


@dataclass  # Item dataclass
class Item:
    name: str
    weight: int


def make_item(name, weight):
    """
    Maker function for item list
    :param name: Name of item
    :param weight: Weight of item
    :return: An item object with name and weight
    """
    return Item(name, int(weight))

def make_box(id, size):
    """
    Maker function for box list
    :param id: Count/id of box
    :param size: Box capacity
    :return: A box object with id and capacity
    """
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
    """
    Performs a greedy insertion sort on a list of items based on weight
    :param items: List of items
    """
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
    :param items: Items list with weight attributes
    :param boxes: Boxes list with capacity attributes
    :return: A tuple of a sorted item list and initial boxes list
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
    Greedy 2 strategy: Sorts items by decreasing weight and place each item in
    the box with the least remaining allowed weight that can support the item.
    If no box can support the item, it is left out.
    :param items: Items list with weight attributes
    :param boxes: Boxes list with capacity attributes
    :return: A tuple of a sorted item list and initial boxes list
    """
    insertion_sort_greedy(items)  # Sort items by decreasing weight
    for item in items:  # Iterate through sorted items list
        box_greedy2 = None
        min_remaining_capacity = 10000  # Initialize with a big value
        for box in boxes:  # Iterate through boxes
            if item.weight <= box.capacity and box.capacity - item.weight < min_remaining_capacity:
                box_greedy2 = box
                min_remaining_capacity = box.capacity - item.weight
        if box_greedy2 is not None:  # If a suitable box is found
            box_greedy2.items.append(item)  # Append item to the chosen box
            box_greedy2.capacity -= item.weight  # Update the box's remaining capacity
        else:
            pass  # Ignore if item cannot go into box
    return (items, boxes)  # Returns a tuple


def greedy3(items, boxes):
    """
    Greedy 3 strategy: Sorts items by decreasing weight and fill the boxes one by one.
    For each box, iterate through all remaining items and place items in the current box.
    :param items: Items list with weight attributes
    :param boxes: Boxes list with capacity attributes
    :return: A tuple of a sorted item list and initial boxes list
    """
    insertion_sort_greedy(items)  # Sort items by decreasing weight
    for box in boxes:  # Iterate through boxes
        remaining_items = list(items)  # Make sorted items list copy
        for item in remaining_items:  # Iterate through the copied items list
            if item.weight <= box.capacity:
                box.items.append(item)  # Append item to the current box
                box.capacity -= item.weight  # Update the box's remaining capacity
                items.remove(item)  # Remove the item from the original list of remaining items
    return (items, boxes)  # Returns a tuple


def output(items, boxes):
    """
    Display the packing results of items into boxes.
    :param items: List of sorted items
    :param boxes: List of sorted boxes
    """
    boxed_items = []
    for box in boxes:
        for items_boxed in box.items:
            boxed_items.append(items_boxed)
    all_items_packed = True  # Assume all items are packed until proven otherwise
    for box in boxes:  # Print details of packed items
        print("Box " + str(box.id) + " of weight capacity " + str(box.size) + " contains:")
        for items_box in box.items:
            print("  " + items_box.name + " of weight " + str(items_box.weight))
    boxed_items = []
    for box in boxes:
        for items_boxed in box.items:
            boxed_items.append(items_boxed)
    for item in items:  # Check if items are left behind
        if item not in boxed_items:
            all_items_packed = False
            print(item.name + " of weight " + str(item.weight) + " got left behind.")
        if all_items_packed:
            print("All items successfully packed into boxes!")
        else:
            print("Unable to pack all items!")

def main():
    """
    Main function for executing item-box allocation greedy strategies.
    """
    user_input = input("What file do you want to select? ")  # Ask for user input
    items, boxes = read(user_input)

    # Copy boxes and items to apply multiple strategies
    boxes1 = [Box([], box.capacity, box.id, box.size) for box in boxes]
    boxes2 = [Box([], box.capacity, box.id, box.size) for box in boxes]
    boxes3 = [Box([], box.capacity, box.id, box.size) for box in boxes]

    items1 = items
    items2 = items
    items3 = items

    # Apply the three greedy strategies
    greedy1(items1, boxes1)
    greedy2(items2, boxes2)
    greedy3(items3, boxes3)

    # Output
    print("Enter datafile name: " + user_input)
    print("")
    print("Results from Greedy Strategy 1")
    output(items1, boxes1)
    print("\n")
    print("Results from Greedy Strategy 2")
    output(items2, boxes2)
    print("\n")
    print("Results from Greedy Strategy 3")
    output(items3, boxes3)


# Main guard
if __name__ == "__main__":
    main()
