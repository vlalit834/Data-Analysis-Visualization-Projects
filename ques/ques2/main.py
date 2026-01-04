import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "data", "netflix.csv")

# 1. Load Netflix dataset
def load_data():
    """
    Load the Netflix dataset from the CSV file inside data/.

    Print:
    - First 5 rows showing: title, type, release_year

    Return:
        Pandas DataFrame
    """

    df = pd.read_csv(DATA_PATH)
    
    print("Dataset loaded successfully!")

    print("\nSample Data (first 5 rows):")
    print(df[df.columns[:3]].head(5))

    return df


# 2. Display basic dataset information
def explore_dataset(df):
    """
    Print dataset shape and column names.
    """

    print("\nDataset Overview:")
    print("Shape of the dataset:", df.shape)
    print("Column Names:", list(df.columns))


# 3. Count Movies vs TV Shows
def count_content_types(df):
    """
    Count and print how many Movies and TV Shows are present.
    """

    print("\nContent Type Distribution:")
    content_counts = df["type"].value_counts()
    print(content_counts)


# 4. Filter content released after 2015
def filter_recent_content(df):
    """
    Filter content released after 2015 and print first 5 rows
    showing title, type, release_year.

    Return:
        Filtered DataFrame
    """

    recent_content = df[df["release_year"]>2015][df.columns[:3]].head(5)
    print("\nContent Released After 2015:")
    print(recent_content)

    return recent_content


# 5. Top 5 most common ratings
def top_ratings(df):
    """
    Print the top 5 most common content ratings.
    """

    print("\nTop 5 Content Ratings:")
    ratings = df["rating"].value_counts().head(5)
    print(ratings)


# 6. Sort content by release year (latest first)
def sort_by_release_year(df):
    """
    Print first 5 rows of latest content sorted by release_year descending.
    """

    sorted_df = df[df.columns[:3]].sort_values(by=["release_year"],ascending=False).head(5)
    
    print("\nLatest Content on Netflix:")
    print(sorted_df)


if __name__ == "__main__":
    print("Netflix Library Explorer Project\n")

    df = load_data()
    explore_dataset(df)
    count_content_types(df)
    recent_df = filter_recent_content(df)
    top_ratings(df)
    sort_by_release_year(df)
