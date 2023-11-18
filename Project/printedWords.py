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
    :return:
    """
    unique = set()  # Initialize set to store unique years
    for word, data in words.items():  # Iterate through input to grab unique years
        unique.update(data.keys())
    sorted_years = sorted(list(unique))  # Convert unique years set into a sorted list
    result = []  # Initialize empty list to store result
    for year in sorted_years:  # Iterate through sorted years and find total count for each year
        total_count = sum(data.get(year, 0) for data in words.values())
        result.append((year, total_count))
    return result

def wordsForYear(year, yearList):
    """
    pass
    :param year:
    :param yearList:
    :return:
    """

