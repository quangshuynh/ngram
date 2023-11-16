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
    letters = "".join(word.lower() for word in words)
    letter_counts = {}
    for letter in list(letters):  # Count occurrence of each letter
        letter_counts[letter] = letters.count(letter)
    graph_values = sorted(letter_counts)
    sorted_letters = sorted(letter_counts, key=letter_counts.get, reverse=True)  # In descending order, sort letters by frequency
    plt.bar(list(graph_values), list([letter_counts[letter] for letter in graph_values]), color="skyblue")  # Plot character counts
    plt.show()
    return "".join(sorted_letters)

