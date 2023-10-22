"""
Computes the optimal location using quick select
file: store_location.py
language: python3
author: Quang Huynh
"""
import time
import sys
import tools as tools
#  import insertion_sort as sort1   # Insertion sort
import select_median as sort2  # Quick sort


def optimal(locations):
    """
    Finds the best location by using quicksort
    :param locations: Number of locations
    :return: Optimal location
    """
    try:
        # sorted_locations = sort1.insertion_sort(locations)
        sorted_locations = sort2.quick_sort(locations)
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

