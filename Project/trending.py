"""
Task 3: Program that computes the top and bottom trending words given starting & ending year.
file: trending.py
language: python3
author: Quang Huynh
"""

import wordData as wd

def trending(words, startYr, endYr):
    """
    Calculates top & bottom trending words between starting & ending year
    :param words: Dictionary mapping words to dictionaries with years and counts.
    :param startYr: Starting year for calculating trending words
    :param endYr: End year for calculating trending words
    :return: A list of tuples containing the word and its trend value
    """
    trending_list = []  # Initialize empty list
    for word, counts in words.items():  # Iterate through & return input dictionary of words & counts
        starting_count = counts.get(startYr, 0)  # Get count for starting year, set to 0 if not present
        end_count = counts.get(endYr, 0)  # Get count for end year, set to 0 if not present
        if starting_count >= 1000 and end_count >= 1000:  # Check if the word meets the requirements
            trend_value = end_count / starting_count  # Calculate trend value
            trending_list.append((word, trend_value))  # Append word & its trend value to list
    trending_list.sort(key=lambda x: x[1], reverse=True)  # Sort the list in decreasing order of trend value
    return trending_list


# Standalone execution
def main():
    file = input("Enter word file: ")  # File name
    words = wd.readWordFile(file)  # Make dictionary
    start = input("Enter starting year: ")  # Starting year
    end = input("Enter ending year: ")  # Ending year
    trending_words = trending(words, int(start), int(end))  # Calculate trends for inbetween start & end year

    # Make top 10 trending words
    top_trend = list(trending_words[idx][0] for idx in range(min(10, len(trending_words))))

    # Make top 10 lowest trending words
    bottom_trend = list(trending_words[idx][0] for idx in range(-1, -11, -1) if idx >= -len(trending_words))

    # Print top 10 trending words inbetween start & end year
    print("The top 10 trending words from " + start + " to " + end + ":\n" + "\n".join(map(str, top_trend)) + "\n")

    # Print top 10 lowest trending words inbetween start & end year
    print("The top 10 trending words from " + start + " to " + end + ":\n" + "\n".join(map(str, bottom_trend)) + "\n")


# Main guard
if __name__ == "__main__":
    main()
