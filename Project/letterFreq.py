"""
Task 1: Program that computes the relative frequency of English characters occurring in print
file: letterFreq.py
language: python3
author: Quang Huynh
"""

import matplotlib.pyplot as plt

def letterFreq(words):
    """
    Computes relative frequency of English characters occurring in print & plot character counts.

    :param words: List of words representing the text for character frequency analysis

    :return: String containing the 26 lowercase characters in the English alphabet, sorted in
    decreasing order of frequency of occurrence of each character.
    """
    letters = "".join(word.lower() for word in words)  # Join lowercase words into a single string
    letter_counts = {}
    for letter in letters:  # Count occurrence of each letter
        letter_counts[letter] = letters.count(letter)
    x_axis = sorted(letter_counts)
    sorted_letters = sorted(letter_counts, key=letter_counts.get,reverse=True)  # In descending order, sort letters by frequency
    plt.bar(x_axis, [letter_counts[letter] for letter in x_axis], color="skyblue")  # Plot character counts
    plt.show()
    return "".join(sorted_letters)

