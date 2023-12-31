import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np
import module1 as t1
import settings


def sentiment():
    df = t1.rename_columns()
    sia = SentimentIntensityAnalyzer()
# Create an empty list to store the sentiments
    sentiments_list = []

    # Iterate through each review text in the 'reviews_text' column
    for review in df['reviews_text']:
        scores = sia.polarity_scores(review)

        positive_score = scores["pos"]
        negative_score = scores["neg"]

        if positive_score > negative_score:
            sentiments_list.append('positive')
        else:
            sentiments_list.append('negative')

    # Add the 'sentiment' column to the DataFrame
    df['sentiment'] = sentiments_list
    return df

def process_text():
    df = sentiment()
    # Tokenize the reviews_text column using nltk's word_tokenize function
    df['reviews_text'] = df['reviews_text'].apply(nltk.word_tokenize)
    df['reviews_text'] = df['reviews_text'].apply(settings.normalize)
    # Normalize the tokenized words using the normalize function from settings

    return df

def export_the_dataset():
    # Call process_text() to get the cleaned dataset with sentiment analysis and tokenization
    df = process_text()
    # Export the cleaned dataset to a new CSV file named 'ecommerce.csv'. use index = False.
    df.to_csv('ecommerce.csv', index=False)
    return df



# TASK 4: Load the Cleaned dataset 'ecommerce.csv' to the database provided.
# follow the instruction in the Task 5 description and complete the task as per it.

# check if mysql table is created using "ecommerce"
# Use this final dataset and upload it on the provided database for performing analysis in MySQL
# To run this task click on the terminal and click on the run project




