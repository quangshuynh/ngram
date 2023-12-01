"""
Task 0: Utility module that defines functions used throughout various tasks
file: wordData.py
language: python3
author: Quang Huynh
"""

def readWordFile(fileName):
    """
    Reads unigram data files and returns a dictionary mapping words to dictionaries.
    :param fileName: String that gives the name of unigram data files. Should not include 'data/',
    only the name of the file inside the data folder
    :return: Dictionary where each word is a key and associated value is another dictionary. Inner
    dictionary has years as keys and counts as values
    """
    path = "data/" + str(fileName)  # Add "data/" before filename
    words = {}  # Initialize empty dictionary
    with open(path, "r") as file:
        current_word = None
        for line in file:  # Loop through each line in file
            line = line.strip()  # Remove leading and trailing whitespace
            if line.isalpha():  # Check if the line is a word
                if current_word is not None:
                    words[str(current_word)] = current_data
                current_word = line
                current_data = {}  # Reset the inner dictionary for each new word
            else:
                year, count = map(int, line.split(","))
                current_data[year] = count
        if current_word is not None:
            words[current_word] = current_data
    return words


def totalOccurrences(word, words):
    """
    Calculates total number of times a word appeared in print
    :param word: Word for which to calculate the count. Not guaranteed to exist in words
    :param words: Dictionary mapping words to dictionaries with years and counts
    :return: Total number of times that the word appeared in print
    """
    if word in words:  # Check if the word is in the words dictionary
        return sum(words[word].values())  # If the word is present, sum the counts for all years
    else:
        return 0   # If the word is not present, return 0


# Standalone execution
def main():
    words = input("Enter word file: ")
    word = input("Enter word: ")
    print("Total occurences of airport: " + totalOccurrences(word, words))

if __name__ == "__main__":
    main()
