"""
Task 4: Program that calculates word similarity based on vector representation of word counts over
multiple years. Each word is treated as a vector in a space defined by the years, with missing counts
represented as zeros. The cosine of the angle between two word vectors is used as the measure of similarity.
file: wordSimilarity.py
language: python3
author: Quang Huynh
"""

import math

def normalize(vector):
    """
    Normalize the given vector
    :param vector:
    :return:
    """
    vector_length = math.sqrt(sum(i ** 2 for i in vector))
    if vector_length != 0:
        normalized_vector = [i / vector_length for i in vector]
    else:
        normalized_vector = vector
    return normalized_vector

def cosine_similarity(vector1, vector2):
    """
    Calculate the cosine similarity between two vectors
    :param vector1:
    :param vector2:
    :return:
    """
    dot_product = sum(vector1[i] * vector2[i] for i in range(len(vector1)))
    return dot_product


def pad_vector(vector, length):
    """
    Pad the vector with zeros to the specified length
    :param vector:
    :param length:
    :return:
    """
    return vector + [0] * (length - len(vector))


def topSimilar(words, word):
    """
    Calculate the top 5 most similar words to the given word based on cosine similarity
    :param words: A dictionary mapping words to dictionaries with years and counts
    :param word: A word for which we are looking for similar words
    :return: A list of the top five words, including the input word, in descending order of similarity
    """
    if word not in words:
        return [word]
    word_vector = list(words[word].values())
    max_length = max(len(word_vector), max(len(v) for v in words.values()))
    normalized_word_vector = normalize(pad_vector(word_vector, max_length))
    similarities = []
    for other_word, other_data in words.items():
        if other_word != word:
            other_vector = list(other_data.values())
            normalized_other_vector = normalize(pad_vector(other_vector, max_length))
            similarity = cosine_similarity(normalized_word_vector, normalized_other_vector)
            similarities.append((other_word, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_similar_words = [word] + [item[0] for item in similarities[:4]]
    return top_similar_words
