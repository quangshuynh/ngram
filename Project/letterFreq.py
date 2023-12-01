"""
Task 1: Program that computes the relative frequency of English characters occurring in print
file: letterFreq.py
language: python3
author: Quang Huynh
"""

import matplotlib.pyplot as plt
import wordData as wd

def letterFreq(words):
    """
    Computes relative frequency of English characters occurring in print & plot character counts.
    :param words: List of words representing the text for character frequency analysis
    :return: String containing the 26 lowercase characters in the English alphabet, sorted in
    decreasing order of frequency of occurrence of each character.
    """
    letter_counts = {}  # Initialize empty dictionary
    for word in words:  # Iterate through each word in list
        count = wd.totalOccurrences(word, words)  # Total number of occurrences
        for letter in word:   # Iterate through each letter in word
            letter_counts[letter] = letter_counts.get(letter, 0) + count  # If the letter is not present, set count to 0 & add current count.
    sorted_letter_counts = dict(sorted(letter_counts.items(), key=lambda x: x[1], reverse=True))  # Dictionary containing letter counts in decreasing other
    sorted_letters = "".join(sorted_letter_counts.keys())  # Add the sorted letters into a single string
    x_axis = sorted(sorted_letter_counts.keys())  # Alphabet for x-axis
    plt.bar(x_axis, [sorted_letter_counts[letter] for letter in x_axis], color="skyblue")  # Plot character counts
    plt.show()
    return sorted_letters


# Standalone execution
def main():
    file = input("Enter word file: ")
    words = wd.readWordFile(file)
    print("Letters sorted by decreasing frequency " + letterFreq(words))


if __name__ == "__main__":
    main()
