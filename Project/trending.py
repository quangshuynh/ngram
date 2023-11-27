"""
Task 3: Program that computes the top and bottom trending words given starting & ending year.
file: trending.py
language: python3
author: Quang Huynh
"""


def trending(words, startYr, endYr):
    """
    Calculates top & bottom trending words between starting & ending year
    :param words: Dictionary mapping words to dictionaries with years and counts.
    :param startYr: Starting year for calculating trending words
    :param endYr: End year for calculating trending words
    :return: A list of tuples containing the word and its trend value
    """

    trending_words = []  # Initialize empty list
    for word, counts in words.items():  # Iterate through input dictionary of words & counts
        starting_count = counts.get(startYr, 0)  # Get count for starting year, set to 0 if not present
        end_count = counts.get(endYr, 0)  # Get count for end year, set to 0 if not present
        if starting_count >= 1000 and end_count >= 1000:  # Check if the word meets the requirements
            trend_value = end_count / starting_count  # Calculate trend value
            trending_words.append((word, trend_value))  # Append word & its trend value to list
    trending_words.sort(key=lambda x: x[1], reverse=True)  # Sort the list in decreasing order of trend value
    return trending_words
