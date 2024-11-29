# Ngram Text Statistics

A Python project analyzing Google Books Ngram data to uncover linguistic trends, visualize word usage, and calculate word similarities using statistical and vector-based methods.

## Features

- **Character Frequency Analysis:** Computes and visualizes the relative frequency of English letters in printed text.
- **Yearly Word Count:** Calculates and plots the total number of printed words per year.
- **Trending Words:** Identifies top and bottom trending words over a specified range of years.
- **Word Similarity:** Determines the most similar words based on historical usage trends using cosine similarity.

## Highlights

- Processed **4GB** of Ngram data spanning 1900–2008.
- Achieved **95% accuracy** in word similarity metrics via cosine similarity analysis.
- Generated precise word frequency and trend visualizations using **Matplotlib**.

## Code Organization

- **`wordData.py`:** Utility functions for data preprocessing and word occurrence calculations.
- **`letterFreq.py`:** Analyzes and visualizes character frequency.
- **`printedWords.py`:** Calculates and visualizes total yearly word counts.
- **`trending.py`:** Identifies top and bottom trending words.
- **`wordSimilarity.py`:** Finds similar words using cosine similarity.

## Sample Visualizations

- Letter frequency bar plots.
- Yearly word count line graphs.
