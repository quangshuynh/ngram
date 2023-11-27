"""
Task 2: Program that computes the total number of printed words for each year
file: printedWords.py
language: python3
author: Quang Huynh
"""

import matplotlib.pyplot as plt

def printedWords(words):
    """
    Calculate the total word count for each year with available data
    :param words: List of words representing the text for character frequency analysis
    :return: A sorted list containing a year and its corresponding total word count
    """
    year_counts = {}  # Initialize empty dictionary
    for word, data in words.items():  # Iterate through input dictionary of words & data
        for year, count in data.items():  # Iterate through data dictionary for each word
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

