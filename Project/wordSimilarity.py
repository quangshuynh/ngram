"""
Task 4: Program that calculates word similarity based on vector representation of word counts over
multiple years. Each word is treated as a vector in a space defined by the years, with missing counts
represented as zeros. The cosine of the angle between two word vectors is used as the measure of similarity.
file: wordSimilarity.py
language: python3
author: Quang Huynh
"""

import numpy as np


def normalize(vector):
    """
    Normalize the given vector
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
    return np.dot(vector1, vector2)


def topSimilar(words, word):
    """
    Calculate the top 5 most similar words to the given word based on cosine similarity
    :param words: A dictionary mapping words to dictionaries with years and counts
    :param word: Input word to find similarities to
    :return: List of the top five words, including the input word, in descending order of similarity
    """
    if word not in words:  # Check if the word is in the dictionary
        return [word]  # Returns a list of the input word if not found
    years = set()  # Initialize set to store unique years for all words
    for input_word, years1 in words.items():  # Iterate through each word and its corresponding years
        years.update(years1.keys())  # Update the years set
    word_vector = np.array([words[word].get(year, 0) for year in sorted(years)])
    normalized = normalize(word_vector)  # Normalize input word vector
    similar_words = {}  # Initialize empty dictionary to store input word & similar words
    for current_word, years2 in words.items():
        vector2 = np.array([years2.get(year, 0) for year in sorted(years)])
        normalized2 = normalize(vector2)  # Normalize current word vector
        similarity = cos_similarity(normalized, normalized2)  # Calculate cosine similarity between input word & current word
        similar_words[current_word] = similarity  # Store similarity with current word as the key
    top_similar_words = sorted(similar_words, key=similar_words.get, reverse=True)[:5]  # Ends at the fifth word
    return top_similar_words  # Returns top five similar words in descending order

# Testing time

if __name__ == "__main__":
    import time
    import wordData as wd


    def test(result, expected):
        if result == expected:
            print("Success")
            return True
        else:
            print("Result: " + str(result) + "\nExpected" + str(expected))
            return False

    def testFile(filename, word, expected):
        file = wd.readWordFile(filename)
        return test(topSimilar(file, word), expected)

    def testing():
        start = time.perf_counter()
        passed = True
        passed = testFile("all.txt", "robot", ["robot", "robots", "robotics", "neuroendocrine", "programmable"]) and passed
        print()
        result = "all.txt success" if passed else "all.txt failed"
        print(str(result))
        print(time.perf_counter() - start)

    testing()


