import pandas as pd

# Function to read the CSV file into a DataFrame
def read_csv():
    df = pd.read_csv("shopping.csv")
    return df

# Function to check for duplicate rows in the DataFrame
def check_duplicates():
    df = read_csv()
    duplicates_count = df.duplicated().sum()
    return duplicates_count

# Function to drop duplicate rows from the DataFrame
def drop_duplicates():
    df = read_csv()
    cleaned_df = df.drop_duplicates()
    return cleaned_df

# Function to check for null (missing) values in the DataFrame
def check_null_values():
    df = read_csv()
    # Calculate the sum of null values for each column
    null_counts = df.isnull().sum()
    # Return the Series containing the count of null values for each column
    return null_counts

# Function to remove rows containing null values from the DataFrame
def remove_null_values():
    df = read_csv()
    df = df.drop_duplicates()
    cleaned_df = df.dropna()
    # Return the cleaned DataFrame with no null values
    return cleaned_df

# Function to rename columns in the DataFrame
def rename_columns():
    df = remove_null_values()
    # Check if the DataFrame is not empty or None
    if df is not None and not df.empty:
        # Define a dictionary to map old column names to new column names
        column_mapping = {
            'reviews.text': 'reviews_text',
            'reviews.title': 'reviews_title',
            'reviews.date': 'reviews_date'
        }
        # Use the rename() method to rename the columns
        df.rename(columns=column_mapping, inplace=True)
    return df


