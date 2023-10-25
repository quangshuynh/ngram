"""
Computes the optimal location using insertion sort
file: store_location.py
language: python3
author: Quang Huynh
"""
import time
import sys
import tools as tools


def insertion_sort(lst):
    """
    Sorts list in ascending order using the insertion sort
    :param lst: List of elements to be sorted
    """
    for mark in range(len(lst) - 1):
        insert(lst, mark)
    return lst


def insert(lst, mark):
    """
    Performs insertion operation in a list to maintain ascending order
    :param lst: List of elements inputted
    :mark: Index at which the element should be inserted
    """
    for index in range(mark, -1, -1):
        if lst[index] > lst[index + 1]:
            swap(lst, index, index + 1)
        else:
            return


def swap(lst, i, j):
    """
    Swap two elements in a list
    :param lst: The list where the elements will be swapped
    :param i: Index of first element to be swapped
    :param j: Index of second element to be swapped
    """
    lst[i], lst[j] = lst[j], lst[i]


def optimal(locations):
    """
    Finds the best location by using insertion sort
    :param locations: Number of locations
    :return: Optimal location
    """
    try:
        sorted_locations = insertion_sort(locations)   # Insertion sort
        if len(sorted_locations) % 2 == 1:  # Calculate the median
            median = sorted_locations[(len(sorted_locations) // 2)]  # Finds median for odd lists
        else:
            m_left = sorted_locations[(len(sorted_locations) // 2) - 1]  # Finds median for even lists
            m_right = sorted_locations[(len(sorted_locations) // 2)]
            median = (m_left + m_right) / 2
        return median
    except TypeError as e:
        print("", end="")


def main():
    """
    Main function that asks user to a text file, reads a list of numbers from it,
    finds the optimal location, calculates the sum of distances to the optimal location,
    and prints the results along with the elapsed time.
    """
    sys.setrecursionlimit(1000000)
    user_input = input("What file do you want to select?: ")
    values = tools.read(user_input)  # List of numbers
    stored_time = time.perf_counter()  # Elapsed time of function
    optimal_location = optimal(values)  # Finding optimal time
    distance_sums = tools.calculate(values, optimal_location)  # Finding sums of distances to optimal location
    print("Enter data file: " + user_input)
    print("Optimum new store location: " + str(optimal_location))
    print("Sum of distances to the new store: " + str(distance_sums))
    print("\nElapsed time:", (time.perf_counter() - stored_time))


# Main guard
if __name__ == "__main__":
    main()
