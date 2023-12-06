"""
Task 4: Program that calculates word similarity based on vector representation of word counts over
multiple years. Each word is treated as a vector in a space defined by the years, with missing counts
represented as zeros. The cosine of the angle between two word vectors is used as the measure of similarity.
file: wordSimilarity.py
language: python3
author: Quang Huynh
"""

import numpy as np
import wordData as wd

def normalize(vector):
    """
    Normalize given vector
    :param vector: Input vector to be normalized
    :return: Normalized vector
    """
    length = np.linalg.norm(vector)  # Calculate length of vector
    if length != 0:  # Check if length is not 0 to avoid dividing by 0
        return vector / length
    else:
        return vector  # If length is 0, return original vector


def cos_similarity(vector1, vector2):
    """
    Calculate the cosine similarity between two vectors
    :param vector1: First vector
    :param vector2: Second vector
    :return: Cosine similarity between vector1 & vector2
    """
    return np.dot(vector1, vector2)  # Dot product of vectors


def topSimilar(words, word):
    """
    Calculate the top 5 most similar words to the given word based on cosine similarity
    :param words: A dictionary mapping words to dictionaries with years and counts
    :param word: Input word to find similarities to
    :return: List of the top five words, including the input word, in descending order of similarity
    """
    if word not in words:  # Check if the word is in the dictionary
        return [word]  # Returns input word if not found
    years = set()  # Initialize set to store unique years for all words / no duplicates
    for input_word, years1 in words.items():  # Iterate through & return input word and its corresponding years
        years.update(years1.keys())  # Update the years set
    word_vector = np.array([words[word].get(year, 0) for year in sorted(years)])
    normalized = normalize(word_vector)  # Normalize input word vector
    similar_words = {}  # Initialize empty dictionary to store input word & similar words
    for current_word, years2 in words.items():  # Iterate through & return current word and its corresponding years
        vector2 = np.array([years2.get(year, 0) for year in sorted(years)])
        normalized2 = normalize(vector2)  # Normalize current word vector
        similarity = cos_similarity(normalized, normalized2)  # Calculate cosine similarity between input word & current word
        similar_words[current_word] = similarity  # Store similarity with current word as the key
    top_similar_words = sorted(similar_words, key=similar_words.get, reverse=True)[:5]  # Ends at the fifth word
    return top_similar_words  # Returns top five similar words in descending order


# Standalone execution
def main():
    """
    Standalone execution for wordSimilarity.py. Asks for name of word file, makes dictionary from the data in the file,
    asks for a word and prints the most similar words of inputted word from the file
    """
    file = input("Enter word file: ")  # Name of file
    words = wd.readWordFile(file)  # Make dictionary
    word = input("Enter word: ")  # Input word to calculate similarity to
    print("The most similar words are: \n" + str(topSimilar(words, word)))  # Print top 5 similar words


# Main guard
if __name__ == "__main__":
    main()
