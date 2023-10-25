"""
Computes the optimal location using quick select
file: select_median.py
language: python3
author: Quang Huynh
"""
import time
import sys
import tools as tools


def quick_select(list):
    """
    Finds the k-th smallest element in a list using the Quickselect
    :param list: Inputted list
    :return: The k-th smallest element from  inputted list.
    """
    try:
        if list == []:
            return []
        else:
            pivot = list[0]
            (less, equal, more) = partition(pivot, list)
            return quick_select(less) + equal + quick_select(more)
    except TypeError as e:
        print("", end="")


def partition(pivot, list):
    """
    Partitions a list into three subgroups (less, equal, more) based on a pivot value.
    :param pivot: Pivot value to partition the list around
    :param list: Input list to be sorted
    :return: Subgroups of values less than, equal to and more than the pivot point
    """
    (less, equal, more) = ([], [], [])
    for e in list:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            equal.append(e)
    return less, equal, more

def optimal(locations):
    """
    Finds the best location by using quicksort
    :param locations: Number of locations
    :return: Optimal location
    """
    try:
        sorted_locations = quick_select(locations)  # Quick select
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

