"""
Task 1: Program that computes the relative frequency of English characters occurring in print
file: letterFreq.py
language: python3
author: Quang Huynh
"""

import matplotlib.pyplot as plt

def letterFreq(words):
    """
    Computes relative frequency of English characters occurring in print

    :param words: Dictionary mapping words to dictionaries with years and counts

    :return: String containing the 26 lowercase characters in the English alphabet, sorted in
    decreasing order of frequency of occurrence of each character.
    """
    letters = "".join([word.lower() for word in words])  # Extract all letters from words
    letter_counts = {letter: letters.count(letter) for letter in set(letters)}  # Count occurrence of each letter
    sorted_letters = sorted(letter_counts, key=letter_counts.get, reverse=True)  # In descending order, sort letters by frequency
    plt.bar(list(letters), list(letter_counts), color="skyblue")  # Plot character counts
    plt.show()
    return "".join(sorted_letters)

