"""
Task 2: Program that computes the total number of printed words for each year
file: printedWords.py
language: python3
author: Quang Huynh
"""

import matplotlib.pyplot as plt
import wordData as wd


def printedWords(words):
    """
    Make a list of for the total count of words each year from a dictionary
    :param words: List of words representing the text for character frequency analysis
    :return: A sorted list containing a year and its corresponding total word count
    """
    year_counts = {}  # Initialize empty dictionary
    for word, info in words.items():  # Iterate through & return input dictionary of words & data
        for year, count in info.items():  # Iterate through & return "info" dictionary value of each word
            if year in year_counts:  # Checks if year is in year_counts
                year_counts[year] += count  # Add word count to current year total
            else:  # If year is not in year_counts
                year_counts[year] = count  # Initialize total word count for year
    x_axis = sorted(year_counts.keys())  # Years for x-axis
    plt.plot(x_axis, [year_counts[year] for year in x_axis])  # Plot total printed words for each year
    plt.show()
    total_words = sorted(year_counts.items())  # Sorted word counts
    return total_words


def wordsForYear(year, yearList):
    """
    Counts words for a specific year from list of year-count pairs
    :param year: Target year for which desired word count
    :param yearList: List of year-count pairs.
    :return: Count of words for specified year. Returns 0 if year is not found in the list
    """
    for current_year, count in yearList:  # Iterate through each year-count pair in list
        if current_year == year:  # Checks if current year is equal to target year
            return count
    return 0  # Return 0 if target year is not found in list


# Standalone execution
def main():
    file = input("Enter word file: ")  # Name of file
    year = str(input("Enter year: "))  # Year to check
    words = wd.readWordFile(file)  # Make dictionary
    words_list = printedWords(words)  # Make list
    count_for_year = str(wordsForYear(int(year), words_list))  # Count words for specified year
    print("Total printed words for " + year + ": " + count_for_year)  # Print amount of words for specified year


# Main guard
if __name__ == "__main__":
    main()
